import os
import pandas as pd
from core.config import settings
import pandas as pd
from datetime import datetime, timedelta
from sklearn.metrics import f1_score
import shutil
import joblib
import csv

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from model.utils import map_gender
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from model.utils import map_gender
import core.lw_log as lw_log
from database.conect_database import conect


# Initialize Supabase client

# Load data of SQL
async def load_data(number_itera=2):
    response = conect.client.table("body_performance")\
                .select("*", count="exact")\
                .order("id", desc=True)\
                .execute()
    
    df = pd.DataFrame(response.data)
    df_last = df.tail(10)
    
    columnas_a_eliminar = ['id', 'created_at']

    df_last.drop(columns=columnas_a_eliminar, inplace=True, errors='ignore')

    save_concat(df_last)


# Concat CSV and save
def save_concat(clean_df):
    try:
        # Leer los dos archivos
        df1 = pd.read_csv(settings.clean_data_path)
        df_total = pd.concat([df1, clean_df], ignore_index=True)
        df_total.to_csv(settings.combined_data, index=False)
        print("Archivos combinados y guardados como:", settings.combined_data)
        model_b()
    except Exception as e:
        print("Error al combinar los archivos:", e)

# def map_gender(X):
#     gender_map = {'M': 0, 'F': 1}
#     X = X.copy()
#     X['gender'] = X['gender'].map(gender_map)
#     return X
# Entrenamiento del modelo B, datos combinados
def model_b():
    try:
        df_model = pd.read_csv(settings.combined_data)

        class_map = joblib.load(settings.class_map_path)

        df_model['class'] = df_model['class'].map(class_map)

        # gender_map = joblib.load(settings.gender_map_path)
        # df_model['gender'] = df_model['gender'].map(gender_map)

        X = df_model.drop(columns=['class'])
        y = df_model['class']

        # Dividir datos
        XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=42)



        # gender_mapper = FunctionTransformer(map_gender)
        gender_mapper = FunctionTransformer(map_gender)
        preprocessor = Pipeline([
        ('gender_mapper', gender_mapper)
        ])

        gb = GradientBoostingClassifier(random_state=42, n_iter_no_change=5, validation_fraction=0.1, tol=1e-4 )
        param_dist = {
            'model__n_estimators': [200, 250, 300],
            'model__learning_rate': [0.005, 0.01, 0.03],  
            'model__max_depth': [2, 3],                   
            'model__min_samples_leaf': [3, 5, 7],         
            'model__min_samples_split': [5, 10, 15],      
            'model__subsample': [0.6, 0.7, 0.75, 0.8, 0.9],          
            'model__max_features': ['sqrt', 'log2'] 
        }
        pipeline = Pipeline([
            ('preprocessing', preprocessor),
            ('model', gb)
        ])
    # StratifiedKFold mantiene la proporción de clases en cada fold
        random_search = RandomizedSearchCV(
            estimator=pipeline,
            param_distributions=param_dist,
            n_iter=50,
            scoring='accuracy',
            cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
            verbose=1,
            random_state=42,
            n_jobs=-1, 
        )


        random_search.fit(XTrain, yTrain)
        print("Mejores parámetros:", random_search.best_params_)

        # best_gb = random_search.best_estimator_

        # Matriz de confusión
        # print("Matriz de confusión:\n")
        # y_pred = random_search.predict(XTest)
        # print(confusion_matrix(yTest, y_pred))
        # # Reporte de clasificación
        # print(classification_report(yTest, y_pred))
        #validate(y_test, y_pred, y_train, X_train, clf)
        # Guardar el modelo
        joblib.dump(random_search.best_estimator_, settings.model_path_B)
        # print("Modelo guardado como :", settings.model_path_B)
        
        comparar_y_reemplazar_modelo(XTest, yTest, settings.model_path_A, settings.model_path_B)

    except Exception as e:
            print("Error al combinar los archivos:", e)


def comparar_y_reemplazar_modelo(X_val, y_val, path_a, path_b, umbral_mejora=0.10):
    # Cargar modelos
    modelo_a = joblib.load(path_a)
    modelo_b = joblib.load(path_b)

    # Hacer predicciones
    pred_a = modelo_a.predict(X_val)
    pred_b = modelo_b.predict(X_val)

    # Calcular métricas
    f1_a = f1_score(y_val, pred_a, average="macro", zero_division=1)
    f1_b = f1_score(y_val, pred_b, average="macro", zero_division=1)

    lw_log.write_log(f"🤖 F1 modelo A: {f1_a:.4f}")
    lw_log.write_log(f"🤖 F1 modelo B: {f1_b:.4f}")
    mejora = f1_b - f1_a

    # Guardar histórico

    try:
        os.makedirs("csv", exist_ok=True)
        with open(settings.test_data_logs, "a", newline="") as f:
            writer = csv.writer(f)
            if f.tell() == 0:  # Si el archivo está vacío, escribir encabezados
                writer.writerow(["timestamp", "f1_model_a", "f1_model_b", "improvement", "model_replaced"])
            writer.writerow([datetime.utcnow().isoformat(), f1_a, f1_b, mejora, mejora >= umbral_mejora])
    except Exception as e:
        print(f"Error al guardar el histórico: {e}")

    # Comparar mejoras
    
    if mejora >= umbral_mejora:
        shutil.copy(path_b, path_a)
        lw_log.write_log(f"✅ Modelo B reemplazó a A (mejora de {mejora:.2%})")
        return True
    else:
        lw_log.write_log(f"❌ No hay mejora suficiente. Se mantiene el modelo A.")
        return False
    