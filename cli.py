# mon_projet/cli.py

import click

@click.command()
@click.option('--nom', prompt='Votre nom', help='Le nom de la personne.')
def bonjour(nom):
    """Affiche un message de bienvenue."""
    click.echo(f"Bonjour, {nom}!")

if __name__ == "__main__":
    bonjour()
