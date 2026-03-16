import paramiko
import os

# Informations VM
VM_HOST = "172.16.133.5"
VM_USER = "ismanuel"           # ou un autre utilisateur SSH
VM_PASS = "abcd"    # mot de passe SSH de la VM

# Informations MariaDB
DB_USER = "ismael"
DB_PASS = "abcd"
DB_NAME = "WMS_BASE"

# Dossier de sauvegarde sur ton PC
LOCAL_BACKUP_DIR = r"D:\Notes Cours Epsi\B3\export_sql"
os.makedirs(LOCAL_BACKUP_DIR, exist_ok=True)

# Nom du fichier SQL que tu vas récupérer
SQL_FILE = f"{DB_NAME}_backup.sql"
REMOTE_SQL_PATH = f"/tmp/{SQL_FILE}"
LOCAL_SQL_PATH = os.path.join(LOCAL_BACKUP_DIR, SQL_FILE)

# Commande mysqldump exécutée dans la VM
DUMP_CMD = (
    f"mysqldump -u{DB_USER} -p{DB_PASS} {DB_NAME} > {REMOTE_SQL_PATH}"
)

def main():
    print("Connexion SSH à la VM…")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(VM_HOST, username=VM_USER, password=VM_PASS)

    print("Exécution du mysqldump…")
    stdin, stdout, stderr = ssh.exec_command(DUMP_CMD)
    stdout.channel.recv_exit_status()  # attendre la fin

    print("Téléchargement du fichier SQL…")
    sftp = ssh.open_sftp()
    sftp.get(REMOTE_SQL_PATH, LOCAL_SQL_PATH)
    sftp.remove(REMOTE_SQL_PATH)
    sftp.close()

    ssh.close()

    print(f"✅ Sauvegarde terminée ! Fichier disponible ici :")
    print(f"➡️  {LOCAL_SQL_PATH}")


if __name__ == "__main__":
    main()