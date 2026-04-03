# Guide d'installation du projet

Ce document explique comment télécharger le projet depuis GitHub, créer un environnement Python, accéder au projet et installer ses dépendances.

Cela est a effectuer depuis n'importe qu'elle environement Linux
Assurer vous que votre utilisateur est les droits sudo

---

## 1. Cloner le projet depuis GitHub

Pour récupérer le projet sur votre machine, utilisez la commande suivante dans votre terminal :

```bash
git clone https://github.com/Fonnolossa/MSPR_2.git
```

Ensuite, accédez au dossier du projet :
```bash
cd MSPR_2
```

## 2. Créer un environnement Python 3.12
Il est recommandé d’utiliser un environnement virtuel pour isoler les dépendances du projet.

1. Assurez-vous que Python 3.12 est installé sur votre machine :
```bash
python3.12 --version
```

2. Créez l’environnement virtuel :
```bash
python3.12 -m venv env
```

3. Activez l’environnement :
```bash
source env/bin/activate
```

## 3. Installer les dépendances

Le projet contient un fichier requirements.txt listant toutes les dépendances nécessaires.

Installez-les avec :
```bash
pip install -r requirements.txt
```

# 4. Lancer le projet
Une fois les dépendances installées, vous pouvez exécuter le projet selon les instructions spécifiques à votre application (par exemple, lancer un script principal) :
```bash
python3.12 Start/main.py
```