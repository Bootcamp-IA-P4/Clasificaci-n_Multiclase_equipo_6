import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from utils import map_gender



current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
data_dir = os.path.join(parent_dir, "data")
csv_path = os.path.join(data_dir, "bodyPerformance.csv")


df_model = pd.read_csv(csv_path)


gender_map = joblib.load(os.path.join('gender_map.pkl'))
class_map = joblib.load(os.path.join('class_map.pkl'))


df_model['class'] = df_model['class'].map(class_map)


X = df_model.drop(columns=['class'])
y = df_model['class']

# Dividir datos
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=42)



gender_mapper = FunctionTransformer(map_gender)
preprocessor = Pipeline([
    ('gender_mapper',gender_mapper)
])

gb = GradientBoostingClassifier(random_state=42)

param_dist = {
    'model__n_estimators': [100, 200],
    'model__learning_rate': [0.05, 0.1],
    'model__max_depth': [3, 5],
}

pipeline = Pipeline([
    ('preprocessing', preprocessor),
    ('model', gb)
])
# Búsqueda de hiperparámetros, StratifiedKFold mantiene la proporción de clases en cada fold
random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=param_dist,
    n_iter=8,
    scoring='accuracy',
    cv=StratifiedKFold(n_splits=3, shuffle=True, random_state=42),
    verbose=1,
    random_state=42,
    n_jobs=-1
)


random_search.fit(XTrain, yTrain)
print("Mejores parámetros:", random_search.best_params_)


best_gb = random_search.best_estimator_

pipeline_path = os.path.join('model.pkl')
joblib.dump(best_gb, pipeline_path)
print(f"Modelo entrenado guardado en: {pipeline_path}")


y_train_pred = best_gb.predict(XTrain)
y_test_pred = best_gb.predict(XTest)

print("Accuracy en train:", accuracy_score(yTrain, y_train_pred))
print("Accuracy en test:", accuracy_score(yTest, y_test_pred))
print("F1-score en train:", f1_score(yTrain, y_train_pred, average='weighted'))
print("F1-score en test:", f1_score(yTest, y_test_pred, average='weighted'))

train_acc = accuracy_score(yTrain, y_train_pred)
test_acc = accuracy_score(yTest, y_test_pred)
diff = train_acc - test_acc

if diff < 0.5:
    print("\n✅ No hay señales evidentes de overfitting.")