class Settings:
    def __init__(self):
        self.model = ""  # Model name
        self.model_type = "MultiClass"  # Model type
        self.model_path_A = "data/model_clf.pkl"

        self.proyect_name = "My body performance"
        self.repository = "https://api.github.com/repos/Bootcamp-IA-P4/Clasificaci-n_Multiclase_equipo_6"
        self.version = "1.0.0"
        self.description = "Assessment of body performance in the sports context"

        self.api_prefix = "/api"
        self.api_version = "/v1"
        self.creators = ["Nhoeli", "Mariela", "Juan Carlos", "Michael"]
        self.datos_prueba = [
    {
        "age": 25,
        "gender": "M",
        "height_cm": 175.0,
        "weight_kg": 72.0,
        "body_fat_%": 16.5,
        "diastolic": 78,
        "systolic": 125,
        "gripForce": 50.0,
        "sit_and_bend_forward_cm": 17.5,
        "sit_ups_counts": 55,
        "broad_jump_cm": 240,
        "class": "A"
    },
    {
        "age": 30,
        "gender": "F",
        "height_cm": 162.0,
        "weight_kg": 60.0,
        "body_fat_%": 24.0,
        "diastolic": 80,
        "systolic": 120,
        "gripForce": 28.0,
        "sit_and_bend_forward_cm": 20.0,
        "sit_ups_counts": 40,
        "broad_jump_cm": 185,
        "class": "B"
    },
    {
        "age": 22,
        "gender": "M",
        "height_cm": 180.0,
        "weight_kg": 82.0,
        "body_fat_%": 20.0,
        "diastolic": 85,
        "systolic": 135,
        "gripForce": 56.0,
        "sit_and_bend_forward_cm": 15.0,
        "sit_ups_counts": 60,
        "broad_jump_cm": 255,
        "class": "A"
    },
    {
        "age": 35,
        "gender": "F",
        "height_cm": 158.0,
        "weight_kg": 68.0,
        "body_fat_%": 28.5,
        "diastolic": 88,
        "systolic": 130,
        "gripForce": 25.0,
        "sit_and_bend_forward_cm": 12.0,
        "sit_ups_counts": 35,
        "broad_jump_cm": 160,
        "class": "C"
    }
]

settings = Settings()
