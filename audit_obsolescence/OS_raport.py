import csv
from platform import release
import requests
import json
from pathlib import Path
from datetime import datetime

file_path = "JSON_Fichier/OS_status.json"

Resultat = {}

def verif_date(eol_date_str):
    # format exemple : "2025-12-31"
    eol_date = datetime.strptime(eol_date_str, "%Y-%m-%d")
    now = datetime.now()

    delta = (eol_date - now).days

    if delta < 0:
        return "Version non supportee"
    elif delta <= 90:
        return "Bientot non supportee"
    else:
        return "Version supportee"

with open('audit_obsolescence/OS.csv', newline='', encoding='utf-8') as csvfile:
    lecteur = csv.reader(csvfile, delimiter=',')
    next(lecteur)  
    for ligne in lecteur:
        OS = ligne[0]
        release = ligne[1]
        API_URL = f"https://endoflife.date/api/v1/products/{OS}/releases/{release}"
        question = requests.get(API_URL)
        if question.status_code == 200:
            reponse = question.json()
            Resultat[OS + " " + release] = reponse["result"]["eolFrom"]
        
        elif question.status_code == 304:
            print("La requete n'as pas été modifiée depuis la dernière fois que vous l'avez vérifiée.")
            print(f"{OS} : {release}")
        elif question.status_code == 404:
            print("L'OS que vous avez entré n'est pas dans la base de données ou n'est pas valide.")
            print(f"{OS} : {release}")
        elif question.status_code == 429:
            print("Le server a reçu trop de requêtes de votre part. Veuillez réessayer plus tard.")
            print(f"{OS} : {release}")
        else:
            print(f"Erreur non gérée: {question.status_code}")
            print(f"{OS} : {release}")
            
    print("\nRésultats de la vérification de l'EOL :")

    for os_release, eol_date in Resultat.items():
        
        status = verif_date(eol_date)

        if Path(file_path).exists():
            with open(file_path, 'r') as f:
                data = json.load(f)
        else:
            data = []
            
        data_dict = {item["os_release"]: item for item in data}
        
        data_dict[os_release] = {
            "os_release": os_release,
            "eol_date": eol_date,
            "status": status
        }
        
        data = list(data_dict.values())
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

