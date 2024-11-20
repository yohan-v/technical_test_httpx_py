# Test technique

Enoncé : Ecrire un client Python basé sur httpx.AsyncClient qui gère une stratégie de retry, par exemple qui est résilient à 2 httpcore.ConnectError.
Les tests unitaires de ce client doivent vérifier si le bon nombre de retry est bien pris en compte.

## Prérequis

Avant de commencer, assurez-vous que les outils suivants sont installés sur votre machine :

- **Python** (>= 3.8)
- **Poetry**
- **Pre-commit**

## Installation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/votre-projet.git
   cd votre-projet
   ```

2. Installez les dépendances avec poetry :

    ```bash
    poetry install
    ```

3. Activez l’environnement virtuel Poetry :
    ```bash
    poetry shell
    ```

4. Configurez les hooks pre-commit :
    ```bash
    pre-commit install
    ```

## Intégration avec pre-commit

pre-commit est configuré pour automatiser des vérifications comme le linting, la validation des formats de code, etc.

Les hooks configurés incluent :
	•	flake8 : Analyse statique de code
	•	black : Formatage automatique
	•	isort : Organisation des imports

Pour exécuter manuellement les hooks sur tous les fichiers :

```bash
pre-commit run -all-files
```
