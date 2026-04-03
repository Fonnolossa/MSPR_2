from dotenv import load_dotenv
import paramiko
import os

load_dotenv()

VM_HOST = os.getenv("VM_HOST")
VM_USER = os.getenv("VM_USER_BACKUP")
VM_PASS = os.getenv("VM_PASS")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

LOCAL_BACKUP_DIR = r"Sauvegarde_SQL"
os.makedirs(LOCAL_BACKUP_DIR, exist_ok=True)

SQL_FILE = f"{DB_NAME}_backup.sql"
REMOTE_SQL_PATH = f"/tmp/{SQL_FILE}"
LOCAL_SQL_PATH = os.path.join(LOCAL_BACKUP_DIR, SQL_FILE)

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