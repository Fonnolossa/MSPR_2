import requests

def get_debian_eol(API_URL):
    
        question = requests.get(API_URL)
        
        if question.status_code == 200:
            reponse = question.json()
            for element in reponse["result"]["releases"]:
                print(f"Nom : {element["codename"]}")
                print(f"Version: {element["name"]}")
                print(f"Date de fin de support: {element["eolFrom"]}")
                print("---------------------------------")
        
        elif question.status_code == 304:
            print("La requete n'as pas été modifiée depuis la dernière fois que vous l'avez vérifiée.")
        
        elif question.status_code == 404:
            print("L'OS que vous avez entré n'est pas dans la base de données ou n'est pas valide.")
            
        elif question.status_code == 429:
            print("Le server a reçu trop de requêtes de votre part. Veuillez réessayer plus tard.")
        
        else:
            print(f"Erreur non gérée: {question.status_code}")
        

if __name__ == "__main__":
    
    OS = str(input("Enter l'OS que vous voulez vérifier: "))
    print("---------------------------------")
    
    API_URL = f"https://endoflife.date/api/v1/products/{OS}"
    
    get_debian_eol(API_URL)