import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

# Import de ton module (assure-toi qu'il s'appelle bien diag_ad_dns.py)
import Diag_AD_DNS

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
        console.print("[q] [red]Quitter[/red]")

        # Demande à l'utilisateur de choisir
        choix = Prompt.ask("\n[bold white]Entrez votre choix[/bold white]", choices=["1", "2", "3", "q", "Q"])

        if choix == "1":
            console.clear()
            console.print("[bold green]Lancement du Module de Diagnostic...[/bold green]\n")

            # Exécution de ton script
            Diag_AD_DNS.run_ad_dns_diagnostic()

            # Pause avant de retourner au menu
            Prompt.ask("\n[dim]Appuyez sur Entrée pour revenir au menu...[/dim]")

        elif choix == "2":
            console.print("\n[yellow]Le module de sauvegarde n'est pas encore prêt ![/yellow]")
            time.sleep(2)

        elif choix == "3":
            console.print("\n[yellow]Le module d'audit n'est pas encore prêt ![/yellow]")
            time.sleep(2)

        elif choix.lower() == "q":
            console.print("\n[bold red]Fermeture de NTL-SysToolbox. Au revoir ![/bold red]")
            sys.exit(0)


if __name__ == "__main__":
    menu_principal()
