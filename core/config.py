class Settings:
    def __init__(self):
        self.model = "GradientBoosting"  # Model name
        self.model_type = "MultiClass"  # Model type
        self.model_path_A = "model/model.pkl"
        self.model_path_B = "model/model_b.pkl"
        self.class_map_path = "model/class_map.pkl"
        self.gender_map_path = "model/gender_map.pkl"
        self.proyect_name = "Rendimiento Corporal"
        self.csv_clean_path = "data/clean_data.csv"
        self.clean_data_path = "data/clean_data.csv"
        self.combined_data = "data/combined_data.csv"
        self.test_data_logs = "data/test_data_logs.csv"
        self.repository = "https://api.github.com/repos/Bootcamp-IA-P4/Clasificaci-n_Multiclase_equipo_6"
        self.version = "1.0.0"
        self.description = "¿Estás preparándote para una oposición física? ¿Entrenas en un gimnasio o simplemente te interesa conocer tu rendimiento corporal?"
        self.slogan = "¡Comienza a clasificar tu rendimiento físico aquí!"
        self.api_prefix = "/api"
        self.api_version = "/v1"
        self.creators = ["Nhoeli", "Mariela", "Juan Carlos", "Michael"]


settings = Settings()
