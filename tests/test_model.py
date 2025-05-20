import unittest
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def map_gender(X):
    gender_map = {'M': 0, 'F': 1}
    X = X.copy()
    X['gender'] = X['gender'].map(gender_map)
    return X

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
model_path = os.path.join(parent_dir, 'model', 'model.pkl')
data_path = os.path.join(parent_dir, 'data', 'bodyPerformance.csv')

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = joblib.load(model_path)
        df = pd.read_csv(data_path)
        self.X = df.drop(columns=['class'])

    def test_model_loaded(self):
        self.assertIsNotNone(self.model, "El modelo no se ha cargado correctamente.")

    def test_input_integrity(self):
        self.assertFalse(self.X.isnull().values.any(), "Los datos de entrada contienen valores nulos.")
        columns = {'age','gender','height_cm','weight_kg','body fat_%','diastolic','systolic','gripForce','sit and bend forward_cm','sit-ups counts','broad jump_cm'}
        self.assertTrue(columns.issubset(set(self.X.columns)), "Faltan columnas en los datos de entrada.")

    def test_model_run(self):
        sample = self.X.sample(10, random_state=42)
        try:
            preds = self.model.predict(sample)
            probs = self.model.predict_proba(sample)
            self.assertEqual(len(preds), 10)
            self.assertEqual(probs.shape, (10, self.model.named_steps['model'].n_classes_))
            
        except Exception as e:
            self.fail(f"El modelo falló al predecir: {e}")

    def test_minimum_accuracy(self):
        df = pd.read_csv(data_path)
        class_map = joblib.load(os.path.join(parent_dir, 'model', 'class_map.pkl'))
        df['class'] = df['class'].map(class_map)
        X = df.drop(columns=['class'])
        y = df['class']

        _, XTest, _, yTest = train_test_split(X, y, test_size=0.2, random_state=42)
        y_pred = self.model.predict(XTest)
        accuracy = accuracy_score(yTest, y_pred)
        self.assertGreaterEqual(accuracy, 0.7, "La precisión del modelo es inferior al 70%.")

if __name__ == "__main__":
    unittest.main()