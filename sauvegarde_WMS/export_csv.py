import csv
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

VM_HOST = os.getenv("VM_HOST")
VM_USER = os.getenv("VM_USER_EXPORT")
VM_PASS = os.getenv("VM_PASS")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def export_table_csv(
    host: str,
    user: str,
    password: str,
    database: str,
    table_name: str,
    csv_path: str,
    port: int = 3306,
    delimiter: str = ";"
):
    """
    Exporte une table MariaDB/MySQL en CSV avec les noms de colonnes.
    """

    # Création automatique du dossier si nécessaire
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    try:
        # Connexion MariaDB
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset="utf8mb4"
        )
        cur = conn.cursor()

        # Lecture de la table
        cur.execute(f"SELECT * FROM `{table_name}`")
        rows = cur.fetchall()

        # Noms des colonnes
        column_names = [desc[0] for desc in cur.description]

        # Écriture CSV
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=delimiter)
            writer.writerow(column_names)
            writer.writerows(rows)

        print(f"✅ Export terminé avec succès → {csv_path}")

    except Exception as e:
        print("❌ Erreur lors de l'export :", e)

    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass


# --------------------- EXÉCUTION ---------------------
if __name__ == "__main__":
    export_table_csv(
        host=VM_HOST,
        user=VM_USER,
        password=VM_PASS,
        database=DB_NAME,
        table_name="produits",
        csv_path=r"Sauvegarde_SQL/produits.csv"
    )