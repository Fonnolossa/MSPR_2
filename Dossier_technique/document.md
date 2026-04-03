### Dossier Technique et Fonctionnel – MSPR_2
## 1. Introduction

Le projet MSPR_2 est un outil Python permettant de gérer des diagnostics et audits de systèmes, incluant des fonctionnalités de sauvegarde et d’audit d’obsolescence. Ce document justifie les choix techniques et décrit le fonctionnement global du projet.

## 2. Architecture logique

L’architecture suit une logique modulaire Python :

MSPR_2/
├─ Start/                # Script principal
├─ audit_obsolescence/   # Module d’audit des systèmes obsolètes
├─ diagnostic/           # Module de diagnostic
├─ sauvegarde_WMS/       # Module de sauvegarde
├─ .env.exemple          # Configuration des secrets
├─ requirements.txt      # Dépendances Python
└─ README.md

Chaque module est indépendant, facilitant la maintenance et les évolutions.

## 3. Répartition par modules
Start/ : lance les différents modules via un menu interactif.
audit_obsolescence/ : analyse les versions et composants obsolètes. Référence les sources officielles pour chaque logiciel, avec date de validité.
diagnostic/ : collecte des informations système pour identifier anomalies et risques.
sauvegarde_WMS/ : sauvegarde et restauration des données critiques.
.env.exemple : fichier de configuration pour secrets et variables d’environnement.

## 4. Configuration et gestion des secrets

Le projet utilise un fichier .env pour stocker les secrets (ex. chemins de sauvegarde, identifiants) isolés de l’application.

Avantage : sécurité et portabilité
Compromis : nécessite une vigilance sur les permissions et le versioning (.gitignore inclus pour ne pas committer les secrets).

## 5. Menu interactif

Le menu principal guide l’utilisateur pour :

Lancer un diagnostic
Effectuer une sauvegarde
Réaliser un audit d’obsolescence

Il est conçu pour être simple et lisible, en ligne de commande, permettant une navigation rapide entre les modules.

## 6. Démarche d’audit d’obsolescence
Sources : documentation officielle des logiciels audités
Méthode : vérification des versions installées vs versions supportées
Date de validité : chaque source est datée et mise à jour régulièrement
Compromis : l’outil ne remplace pas un audit manuel complet mais fournit une alerte rapide sur les composants critiques.

## 7. Choix techniques et compromis
Choix technique	Justification	Compromis
Python 3.12	Large écosystème, support des modules système	Dépendance à la version 3.12 spécifique
Modules séparés	Maintenance facile, réutilisation	Complexité de coordination entre modules
Fichier .env	Sécurisation des secrets	Nécessite gestion des permissions
Menu CLI	Simplicité, légèreté	Pas d’interface graphique

## 8. Conclusion

Le projet MSPR_2 est conçu pour être modulaire, sécurisé et facilement maintenable. Les choix techniques sont argumentés et les compromis clairement assumés, permettant une utilisation efficace pour la gestion de diagnostics, sauvegardes et audits d’obsolescence.