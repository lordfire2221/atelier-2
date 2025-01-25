import pandas as pd
import json
from pandas import json_normalize

# Étape 1 : Détecter l'encodage du fichier
file_path = "data/commits.json"

# Lire le fichier en mode binaire pour détecter l'encodage
with open(file_path, "rb") as f:
    raw_data = f.read()
    import chardet
    result = chardet.detect(raw_data)
    detected_encoding = result["encoding"]
    print(f"Encodage détecté : {detected_encoding}")

# Étape 2 : Réencoder en UTF-8 si nécessaire
if detected_encoding != "utf-8":
    with open(file_path, "r", encoding=detected_encoding) as f:
        content = f.read()

    # Sauvegarder le fichier réencodé en UTF-8
    utf8_file_path = "data/commits_utf8.json"
    with open(utf8_file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fichier réencodé en UTF-8 : {utf8_file_path}")

    # Utiliser le fichier UTF-8 pour la conversion
    file_path = utf8_file_path

# Étape 3 : Charger et normaliser les données JSON
try:
    # Charger le fichier JSON
    with open(file_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # Normaliser les données JSON si elles sont imbriquées ou non uniformes
    data = json_normalize(json_data)
    
    # Vérifier si le dossier de destination existe
    import os
    parquet_dir = "data/parquet"
    if not os.path.exists(parquet_dir):
        os.makedirs(parquet_dir)

    # Convertir en Parquet
    parquet_file_path = os.path.join(parquet_dir, "commits.parquet")
    data.to_parquet(parquet_file_path, engine="pyarrow")
    print(f"Conversion en Parquet terminée : {parquet_file_path}")

except Exception as e:
    print(f"Une erreur s'est produite : {e}")
