import sys
import time
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console = Console()

def menu_principal():
    while True:
        console.print("\n[bold yellow]Que souhaitez-vous faire ?[/bold yellow]")
        console.print("[1] [green]Script 1 : Liste des composants[/green]")
        console.print("[2] [magenta]Script 2 : OS information[/magenta]")
        console.print("[3] [cyan]Script 3 : Raport d'obsolescence avec CSV [/cyan]")
        console.print("[Q] [red]Quitter[/red]")

        choix = Prompt.ask("\n[bold white]Entrez votre choix[/bold white]", choices=["1", "2", "3", "Q"])

        if choix == "1":
            console.clear()
            console.print("[bold green]Lancement de Liste des composants[/bold green]\n")
            subprocess.run(["sudo", "Python/bin/python3.12", "audit_obsolescence/scan_composant.py"])

        elif choix == "2":
            console.clear()
            console.print("[bold green]Lancement de OS information[/bold green]\n")
            subprocess.run(["python3.12", "audit_obsolescence/info_os.py"])

        elif choix == "3":
            console.clear()
            console.print("[bold green]Lancement de Raport d'obsolescence avec CSV [/bold green]\n")
            subprocess.run(["python3.12", "audit_obsolescence/OS_raport.py"])

        elif choix == "Q":
            console.print("\n[bold red]Fermeture de NTL-SysToolbox. Au revoir ![/bold red]")
            console.clear()
            sys.exit(0)


if __name__ == "__main__":
    menu_principal()
