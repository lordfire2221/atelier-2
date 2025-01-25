import pandas as pd
import json
from pandas import json_normalize
import os
import chardet

# Fonction pour détecter l'encodage
def detect_encoding(file_path):
    with open(file_path, "rb") as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result["encoding"]

# Fonction pour réencoder en UTF-8
def reencode_to_utf8(file_path, detected_encoding):
    utf8_file_path = file_path.replace(".json", "_utf8.json")
    try:
        with open(file_path, "r", encoding=detected_encoding) as f:
            content = f.read()
        with open(utf8_file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return utf8_file_path
    except Exception as e:
        print(f"Erreur lors du réencodage de {file_path} : {e}")
        return None

# Fonction pour valider si le fichier JSON est valide
def validate_json(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                print(f"Erreur : Le fichier {json_file} est vide.")
                return False
            json.loads(content)
        return True
    except json.JSONDecodeError as e:
        print(f"Erreur JSON dans {json_file} : {e}")
        return False
    except Exception as e:
        print(f"Erreur inattendue lors de la validation de {json_file} : {e}")
        return False

# Fonction pour charger, normaliser et convertir en Parquet
def process_json_to_parquet(json_file, parquet_dir, table_name):
    # Détecter l'encodage
    detected_encoding = detect_encoding(json_file)
    print(f"Encodage détecté pour {json_file} : {detected_encoding}")

    # Réencoder en UTF-8 si nécessaire
    if detected_encoding != "utf-8":
        json_file = reencode_to_utf8(json_file, detected_encoding)
        if not json_file:
            print(f"Réencodage échoué pour {json_file}.")
            return

    # Valider le fichier JSON avant de continuer
    if not validate_json(json_file):
        print(f"Validation échouée pour {json_file}.")
        return

    # Charger et traiter les données JSON
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        # Vérifier le type des données et les normaliser
        if isinstance(json_data, list):
            data = json_normalize(json_data)
        elif isinstance(json_data, dict):
            data = json_normalize([json_data])  # Convertir un objet dict en liste
        else:
            print(f"Données non prises en charge dans {json_file}.")
            return

        # Vérifier si le dossier cible existe
        if not os.path.exists(parquet_dir):
            os.makedirs(parquet_dir)

        # Sauvegarder les données en Parquet
        parquet_file = os.path.join(parquet_dir, f"{table_name}.parquet")
        data.to_parquet(parquet_file, engine="pyarrow")
        print(f"Conversion en Parquet terminée pour {table_name} : {parquet_file}")

    except Exception as e:
        print(f"Erreur lors du traitement de {json_file} : {e}")

# Définir les fichiers JSON et leur table cible
files = {
    "data/commits.json": "commits",
    "data/issues.json": "issues",
    "data/releases.json": "releases"
}

# Dossier de destination pour les fichiers Parquet
parquet_directory = "data/parquet"

# Traiter chaque fichier JSON
for json_file, table_name in files.items():
    process_json_to_parquet(json_file, parquet_directory, table_name)
