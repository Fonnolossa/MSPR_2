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
        console.print("[1] [green]Script 1 : Sauvegarde de la base de données[/green]")
        console.print("[2] [magenta]Script 2 : EXport de table[/magenta]")
        console.print("[Q] [red]Quitter[/red]")

        choix = Prompt.ask("\n[bold white]Entrez votre choix[/bold white]", choices=["1", "2", "Q"])

        if choix == "1":
            console.clear()
            console.print("[bold green]Lancement de Sauvegarde de la base de données[/bold green]\n")
            subprocess.run(["python3.12", "sauvegarde_WMS/backup_sql.py"])

        elif choix == "2":
            console.clear()
            console.print("[bold green]Lancement de Export de table[/bold green]\n")
            subprocess.run(["python3.12", "sauvegarde_WMS/export_csv.py"])

        elif choix == "Q":
            console.print("\n[bold red]Fermeture de NTL-SysToolbox. Au revoir ![/bold red]")
            console.clear()
            sys.exit(0)


if __name__ == "__main__":
    menu_principal()
