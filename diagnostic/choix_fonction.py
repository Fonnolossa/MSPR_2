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
        console.print("[1] [green]Script 1 : Diagnostic AD & DNS[/green]")
        console.print("[2] [magenta]Script 2 : Diagnostic Mysql[/magenta]")
        console.print("[3] [magenta]Script 3 : Diagnostic Ubuntu[/magenta]")
        console.print("[4] [magenta]Script 4 : Diagnostic Windows server[/magenta]")
        console.print("[Q] [red]Quitter[/red]")

        choix = Prompt.ask("\n[bold white]Entrez votre choix[/bold white]", choices=["1", "2", "3", "4", "Q"])

        if choix == "1":
            console.clear()
            console.print("[bold green]Lancement de Diagnostic AD & DNS[/bold green]\n")
            subprocess.run(["python3.12", "diagnostic/AD_DNS.py"])

        elif choix == "2":
            console.clear()
            console.print("[bold green]Lancement de Diagnostic Mysql[/bold green]\n")
            subprocess.run(["python3.12", "diagnostic/Mysql.py"])

        elif choix == "3":
            console.clear()
            console.print("[bold green]Lancement de Diagnostic Ubuntu[/bold green]\n")
            subprocess.run(["python3.12", "diagnostic/ubuntu.py"])

        elif choix == "4":
            console.clear()
            console.print("[bold green]Lancement de Diagnostic Windows server[/bold green]\n")
            subprocess.run(["python3.12", "diagnostic/windows.py"])

        elif choix == "Q":
            console.print("\n[bold red]Fermeture de NTL-SysToolbox. Au revoir ![/bold red]")
            console.clear()
            sys.exit(0)


if __name__ == "__main__":
    menu_principal()
