import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from model.utils import map_gender
from core.config import settings

df_model = pd.read_csv(settings.csv_clean_path)


gender_map = joblib.load(settings.gender_map_path)
class_map = joblib.load(settings.class_map_path)
df_model['class'] = df_model['class'].map(class_map)


X = df_model.drop(columns=['class'])
y = df_model['class']

# Dividir datos
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=42)



gender_mapper = FunctionTransformer(map_gender)
preprocessor = Pipeline([
    ('gender_mapper',gender_mapper)
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


best_gb = random_search.best_estimator_

pipeline_path = os.path.join('model/model.pkl')
joblib.dump(best_gb, pipeline_path)
print(f"Modelo entrenado guardado en: {pipeline_path}")


y_train_pred = best_gb.predict(XTrain)
y_test_pred = best_gb.predict(XTest)

print("\n=== Métricas de Entrenamiento ===")
print(f"Accuracy:  {accuracy_score(yTrain, y_train_pred):.4f}")
print(f"Precision: {precision_score(yTrain, y_train_pred, average='weighted'):.4f}")
print(f"Recall:    {recall_score(yTrain, y_train_pred, average='weighted'):.4f}")
print(f"F1 Score:  {f1_score(yTrain, y_train_pred, average='weighted'):.4f}")
try:
    y_train_proba = best_gb.predict_proba(XTrain)
    print(f"ROC AUC:   {roc_auc_score(yTrain, y_train_proba, multi_class='ovr'):.4f}")
except Exception as e:
    print(f"ROC AUC:   No calculable ({e})")


print("\n=== Métricas del modelo (Test) ===")
print(f"Accuracy:  {accuracy_score(yTest, y_test_pred):.4f}")
print(f"Precision: {precision_score(yTest, y_test_pred, average='weighted'):.4f}")
print(f"Recall:    {recall_score(yTest, y_test_pred, average='weighted'):.4f}")
print(f"F1 Score:  {f1_score(yTest, y_test_pred, average='weighted'):.4f}")

try:
    y_test_proba = best_gb.predict_proba(XTest)
    print(f"ROC AUC:   {roc_auc_score(yTest, y_test_proba, multi_class='ovr'):.4f}")
except Exception as e:
    print(f"ROC AUC:   No calculable ({e})")
     
train_acc = accuracy_score(yTrain, y_train_pred)
test_acc = accuracy_score(yTest, y_test_pred)
diff = train_acc - test_acc
print(f"\nDiferencia de accuracy entre entrenamiento y test: {diff:.4f}")
if diff < 0.05:
    print("\n✅ No hay señales evidentes de overfitting.")

# Evaluación automática de overfitting
overfitting_percent = ((train_acc - test_acc) / train_acc) * 100

print(f"\n📊 Porcentaje de overfitting: {overfitting_percent:.2f}%")


if overfitting_percent < 3 and test_acc >= 0.80:
    print("✅ Configuración óptima: precisión alta sin overfitting.")
elif overfitting_percent < 5:
    print("🟡 Precaución: ligero overfitting, pero aceptable si la precisión es buena.")
else:
    print("⚠️ Atención: posible overfitting, considera ajustar hiperparámetros.")

