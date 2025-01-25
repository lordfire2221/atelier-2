import duckdb
import os

# Chemin vers la base DuckDB
db_path = "data_lake.duckdb"

# Fichiers JSON à charger
files = {
    "data/commits.json": "raw_commits",
    "data/issues.json": "raw_issues",
    "data/releases.json": "raw_releases"
}

# Connexion à la base DuckDB
conn = duckdb.connect(db_path)

# Création de la table d'historique si elle n'existe pas
conn.execute("""
    CREATE TABLE IF NOT EXISTS load_history (
        table_name VARCHAR,
        file_path VARCHAR,
        load_date TIMESTAMP DEFAULT NOW()
    )
""")

for file_path, table_name in files.items():
    if os.path.exists(file_path):
        try:
            # Charger le fichier JSON dans une table DuckDB
            print(f"Chargement de {file_path} dans la table {table_name}...")
            conn.execute(f"""
                CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_json_auto('{file_path}')
            """)
            print(f"Table {table_name} créée avec succès.")
            
            # Ajouter une entrée dans l'historique
            conn.execute("""
                INSERT INTO load_history (table_name, file_path)
                VALUES (?, ?)
            """, (table_name, file_path))
            print(f"Historisation effectuée pour {table_name}.")
        except Exception as e:
            print(f"Erreur lors du chargement de {file_path} : {e}")
    else:
        print(f"Fichier introuvable : {file_path}")

# Vérification des tables créées
print("\nTables créées dans DuckDB :")
print(conn.execute("SHOW TABLES").fetchall())

# Affichage du contenu de la table d'historique
print("\nContenu de la table d'historique :")
print(conn.execute("SELECT * FROM load_history").fetchall())

# Fermer la connexion
conn.close()
