from database.conect_database import conect
import core.lw_log as lw_log
import pandas as pd

def get_data(gender, age):
    try:
        response_com = (
            conect.client.table("body_performance")
            .select("*")
            .eq("gender", gender)
            .eq("age", age)
            .execute()
        )
        data = response_com.data if hasattr(response_com, 'data') else None
        if not data:
            lw_log.write_log("⚠️ No hay datos de genero o edad.")
            return None
        df = pd.DataFrame(data)
        gripforce_avg = df["gripforce"].mean()
        sit_and_bend_forward_cm_avg = df["sit_and_bend_forward_cm"].mean()
        sit_ups_counts_avg = df["sit_ups_counts"].mean()
        broad_jump_cm_avg = df["broad_jump_cm"].mean()

        lw_log.write_log(f"✅ Medias:\n {gripforce_avg,  sit_and_bend_forward_cm_avg  , sit_ups_counts_avg, broad_jump_cm_avg}")
        return gripforce_avg,  sit_and_bend_forward_cm_avg  , sit_ups_counts_avg, broad_jump_cm_avg  
    except Exception as e:
        lw_log.write_log(f"❌ Error al obtener los datos: {e}")
        return None