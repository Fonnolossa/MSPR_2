import nmap
import json
from pathlib import Path
import paramiko
import ipaddress

def demander_ipv4_cidr():
    while True:
        cidr_input = input("Entrez une IPv4 avec masque (ex: 192.168.1.0/24) : ").strip()
        try:
            # Cette ligne valide l'IPv4 + le masque
            reseau = ipaddress.IPv4Network(cidr_input, strict=True)
            print(f"Adresse valide : {reseau}")
            return str(reseau)
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez réessayer.")

def analyse_os(hosts,username):
    
    results = {}

    for host in hosts:
        try:
            print(f"Connexion à {host}...")
            
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            ssh.connect(hostname=host, username=username, timeout=5)

            # Installer lsb-release (Debian/Ubuntu)
            install_cmd = "sudo apt-get update -y && sudo apt-get install -y lsb-release"
            ssh.exec_command(install_cmd)

            # Exécuter la commande
            stdin, stdout, stderr = ssh.exec_command("lsb_release -i")
            output = stdout.read().decode().strip()

            # Stocker dans le dictionnaire
            results[host] = output.split()[-1]

            ssh.close()

        except Exception as e:
            results[host] = f"Erreur: {str(e)}"
            
    return results

def detect_os(target):

    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-O')  # -O = OS detection

    Resultat = {}
    
    for host in nm.all_hosts():
        if 'osmatch' in nm[host]:
            for os in nm[host]['osmatch']:
                if os["name"].split()[0] == "Microsoft":
                    if "Windows Server" in os["name"]:
                        Resultat[host] = "windows-server"# Stocke seulement le nom de l'OS sans la version
                    else :
                        Resultat[host] = "windows"# Stocke seulement le nom de l'OS sans la version
                else :
                    Resultat[host] = os['name'].split()[0]# Stocke
                break  # Affiche seulement le premier résultat d'OS détecté
    
    return Resultat

def creaction_json(result):
    
    file_path = "JSON_Fichier/ScanResult.json"
    
    for host_2, os_2 in result.items():
        
        if Path(file_path).exists():
            with open(file_path, 'r') as f:
                data = json.load(f)
        else:
            data = []

        data_dict = {item["host"]: item for item in data}

        data_dict[host_2] = {
            "host": host_2,
            "os": os_2
        }

        data = list(data_dict.values())

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    
    return None
    


        
if __name__ == "__main__":
    
    target = demander_ipv4_cidr()
    print(f"Scan en cours sur la plage {target}...")
    print("------------------------------")
    result = detect_os(target) 
    print("\nRésultats de la détection d'OS :")
    Linuxs = []
    for host, os in result.items():
        if os == "Linux":
            Linuxs.append(host)
    resultat = analyse_os(Linuxs,"g2")
    result.update(resultat)
    creaction_json(result)
