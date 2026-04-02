import nmap

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
        
if __name__ == "__main__":
    
    target = "192.168.1.0/24"
    result = detect_os(target) 
    print("\nRésultats de la détection d'OS :")
    for host, os in result.items():
        print(f"{host} : {os}")