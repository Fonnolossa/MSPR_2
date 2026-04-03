import sys
import time
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

# Initialisation de la console
console = Console()


def afficher_en_tete():
    """Affiche une jolie bannière au démarrage sans casser l'ASCII art"""
    console.clear()

    # ASCII Art corrigé pour "NTL-SysToolbox"
    ascii_art = r"""
  _   _ _______ _            _____           _______          _ _               
 | \ | |__   __| |          / ____|         |__   __|        | | |              
 |  \| |  | |  | |  ______ | (___  _   _ ___   | | ___   ___ | | |__   _____  __
 | . ` |  | |  | | |______| \___ \| | | / __|  | |/ _ \ / _ \| | '_ \ / _ \ \/ /
 | |\  |  | |  | |____      ____) | |_| \__ \  | | (_) | (_) | | |_) | (_) >  < 
 |_| \_|  |_|  |______|    |_____/ \__, |___/  |_|\___/ \___/|_|_.__/ \___/_/\_\
                                    __/ |                                       
                                   |___/                                        
"""

    texte_brut = Text(ascii_art, style="bold cyan")

    panneau = Panel(
        texte_brut,
        title="[bold white]Projet MSPR - Groupe 3[/bold white]",
        border_style="blue",
        expand=False
    )
    console.print(panneau)


def menu_principal():
    while True:
        afficher_en_tete()

        console.print("\n[bold yellow]Que souhaitez-vous faire ?[/bold yellow]")
        console.print("[1] [green]Module 1 : Diagnostic AD, DNS et Système[/green]")
        console.print("[2] [magenta]Module 2 : Sauvegarde de la base WMS (En construction)[/magenta]")
        console.print("[3] [cyan]Module 3 : Audit d'obsolescence (En construction)[/cyan]")
        console.print("[Q] [red]Quitter[/red]")

        # Demande à l'utilisateur de choisir
        choix = Prompt.ask("\n[bold white]Entrez votre choix[/bold white]", choices=["1", "2", "3", "Q"])

        if choix == "1":
            chemin_script = "diagnostic/choix_fonction.py"
            subprocess.run(["python3.12", chemin_script])
            sys.exit(0)

        elif choix == "2":
            chemin_script = "sauvegarde_WMS/choix_fonction.py"
            subprocess.run(["python3.12", chemin_script])
            sys.exit(0)


        elif choix == "3":
            chemin_script = "audit_obsolescence/choix_fonction.py"
            subprocess.run(["python3.12", chemin_script])
            sys.exit(0)

        elif choix == "Q":
            console.print("\n[bold red]Fermeture de NTL-SysToolbox. Au revoir ![/bold red]")
            sys.exit(0)


if __name__ == "__main__":
    menu_principal()
