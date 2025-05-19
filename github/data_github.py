import requests
from core.config import settings
import core.lw_log as lw_log

def get_latest_github_tag():
    url = settings.repository+"/tags"
    response = requests.get(url)
    if response.status_code == 200:
        tags = response.json()
        if tags:
            v = tags[0]['name']
            lw_log.write_log(f"✅ Última versión: {v}")
            return v  # último tag (ordenado por fecha de commit)
        else:
            lw_log.write_log(f"✅ No hay versión.")
            return "No tags found"
    lw_log.write_log(f"❌ GitHub API error.")
    return ""

def get_repo_info():
    response = requests.get(settings.repository)

    if response.status_code == 200:
        data = response.json()
        print(f"📦 Repositorio: {data['full_name']}")
        print(f"📝 Descripción: {data.get('description', 'Sin descripción')}")
        print(f"⭐ Estrellas: {data['stargazers_count']}")
        print(f"🍴 Forks: {data['forks_count']}")
        print(f"🐞 Issues abiertos: {data['open_issues_count']}")
        print(f"💻 Lenguaje principal: {data.get('language', 'No detectado')}")
        print(f"🔄 Última actualización: {data['updated_at']}")
        print(f"🌿 Rama por defecto: {data['default_branch']}")
        print(f"🔓 Licencia: {data['license']['name'] if data.get('license') else 'No definida'}")
        print(f"👁️ Visibilidad: {'Privado' if data['private'] else 'Público'}")
        lw_log.write_log(f"🏭 {data['full_name']}")
    else:
        print(f"❌ Error al obtener datos: {response.status_code} - {response.text}")
        lw_log.write_log(f"❌ Error al obtener datos: {response.status_code} - {response.text}")

def get_repo_contributors():
    url = settings.repository+"/contributors"
    params = {"sha": "master", "per_page": min(100, 100)}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        contributors = response.json()
        if not contributors:
            lw_log.write_log(f"🤷‍♂️ No hay contribuidores en este repositorio.")
            print("🤷‍♂️ No hay contribuidores en este repositorio.")
            return

        print(f"👨‍💻 Contribuidores del repositorio:")
        for idx, contributor in enumerate(contributors, start=1):
            lw_log.write_log(f"{idx}. {contributor['login']} - {contributor['contributions']} contribuciones")
            print(f"{idx}. {contributor['login']} - {contributor['contributions']} contribuciones")
    else:
        lw_log.write_log(f"❌ Error al obtener contribuidores: {response.status_code} - {response.text}")
        print(f"❌ Error al obtener contribuidores: {response.status_code} - {response.text}")