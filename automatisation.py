import requests
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Configuration
GITHUB_TOKEN = "votre_token_personnel"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}
BASE_URL = "https://api.github.com"

def fetch_data(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur : {response.status_code}")
        return []

# Exemple : Collecte des stars
def get_stars(repo_owner, repo_name):
    data = fetch_data(f"repos/{repo_owner}/{repo_name}/stargazers")
    df = pd.DataFrame(data)
    # Conversion en Parquet
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f"{repo_name}_stars.parquet")
    print(f"Fichier {repo_name}_stars.parquet créé.")

# Utilisation
get_stars("owner", "repository")
