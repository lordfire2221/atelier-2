import os
import subprocess
import json
import pandas as pd

# Répertoires de sortie
OUTPUT_DIR = "data"
PARQUET_DIR = "data/parquet2"

# Créer les répertoires si inexistants
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PARQUET_DIR, exist_ok=True)

# Endpoints GitHub et noms des tables
endpoints = {
    "repo_data": "https://api.github.com/repos/YetiforceCompany/YetiForce",
    "issues": "https://api.github.com/repos/YetiforceCompany/YetiForce/issues",
    "releases": "https://api.github.com/repos/YetiforceCompany/YetiForce/releases",
    "commits": "https://api.github.com/repos/YetiforceCompany/YetiForce/commits"
}

# Fonction pour exécuter GitHub CLI et récupérer les données
def fetch_github_data(endpoint_url, output_file):
    try:
        print(f"Récupération des données depuis {endpoint_url}...")
        subprocess.run(
            ["gh", "api", endpoint_url, "--paginate"],
            stdout=open(output_file, "w"),
            check=True
        )
        print(f"Données enregistrées dans {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la récupération des données depuis {endpoint_url}: {e}")

# Fonction pour convertir JSON en Parquet
# Fonction pour convertir JSON en Parquet avec validation
def convert_to_parquet(json_file, parquet_file):
    try:
        print(f"Conversion de {json_file} en {parquet_file}...")
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Vérifier que les données sont exploitables (liste ou dictionnaire)
        if isinstance(data, dict):
            data = [data]  # Convertir un objet dict en liste pour Pandas
        if not isinstance(data, list):
            print(f"Erreur : Les données dans {json_file} ne sont pas un tableau ou un objet JSON valide.")
            return

        # Convertir en DataFrame Pandas
        df = pd.DataFrame(data)

        # Sauvegarder au format Parquet
        df.to_parquet(parquet_file, engine="pyarrow", index=False)
        print(f"Fichier Parquet créé : {parquet_file}")
    except json.JSONDecodeError as e:
        print(f"Erreur JSON dans {json_file} : {e}")
    except Exception as e:
        print(f"Erreur lors de la conversion de {json_file} en Parquet : {e}")

# Processus principal
for name, url in endpoints.items():
    json_file = os.path.join(OUTPUT_DIR, f"{name}.json")
    parquet_file = os.path.join(PARQUET_DIR, f"{name}.parquet")

    # Étape 1 : Récupérer les données depuis GitHub
    fetch_github_data(url, json_file)

    # Étape 2 : Convertir les données en Parquet
    if os.path.exists(json_file):
        convert_to_parquet(json_file, parquet_file)
    else:
        print(f"Fichier JSON introuvable : {json_file}")

print("\nToutes les données ont été récupérées et converties en Parquet.")
