import argparse

def analyser_log(fichier_log):
    stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    
    try:
        with open(fichier_log, 'r') as f:
            for ligne in f:
                for niveau in stats:
                    if niveau in ligne:
                        stats[niveau] += 1
    except FileNotFoundError:
        print(f"Fichier '{fichier_log}' introuvable.")
        return None
    
    return stats

def generer_rapport(stats, fichier_rapport):
    try:
        with open(fichier_rapport, 'w') as f:
            f.write("=== Rapport d'analyse des logs ===\n")
            for niveau, compteur in stats.items():
                f.write(f"{niveau}: {compteur}\n")
        print(f"Rapport généré dans '{fichier_rapport}'.")
    except Exception as e:
        print(f"Erreur lors de la génération du rapport: {e}")

def main():
    parser = argparse.ArgumentParser(description="Analyseur de logs simple.")
    parser.add_argument('--log', type=str, default='log.txt', help='Chemin du fichier log à analyser')
    parser.add_argument('--output', type=str, default='rapport.txt', help='Chemin du rapport généré')
    
    args = parser.parse_args()
    
    stats = analyser_log(args.log)
    if stats:
        generer_rapport(stats, args.output)

if __name__ == "__main__":
    main()
