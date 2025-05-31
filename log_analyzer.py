#!/usr/bin/env python3
# log_analyzer.py

import argparse
from collections import defaultdict
from colorama import init, Fore

# Initialisation de colorama pour les couleurs dans le terminal
init()

def analyze_logs(input_file='log.txt', output_file='rapport.txt'):
    """
    Analyse un fichier log et génère un rapport avec les statistiques.
    
    Args:
        input_file (str): Chemin vers le fichier log à analyser
        output_file (str): Chemin vers le fichier de sortie
    """
    log_counts = defaultdict(int)
    total_lines = 0

    try:
        with open(input_file, 'r') as f:
            for line in f:
                total_lines += 1
                line = line.strip().upper()
                if 'ERROR' in line:
                    log_counts['ERROR'] += 1
                elif 'WARNING' in line:
                    log_counts['WARNING'] += 1
                elif 'INFO' in line:
                    log_counts['INFO'] += 1
                else:
                    log_counts['OTHER'] += 1

        # Génération du rapport
        with open(output_file, 'w') as f:
            f.write(f"Rapport d'analyse du fichier {input_file}\n")
            f.write("="*40 + "\n")
            f.write(f"Total de lignes analysées: {total_lines}\n")
            f.write(f"ERROR: {log_counts['ERROR']}\n")
            f.write(f"WARNING: {log_counts['WARNING']}\n")
            f.write(f"INFO: {log_counts['INFO']}\n")
            f.write(f"OTHER: {log_counts['OTHER']}\n")

        # Affichage coloré dans le terminal
        print(Fore.RED + f"ERRORS: {log_counts['ERROR']}" + Fore.RESET)
        print(Fore.YELLOW + f"WARNINGS: {log_counts['WARNING']}" + Fore.RESET)
        print(Fore.GREEN + f"INFOS: {log_counts['INFO']}" + Fore.RESET)
        print(f"Autres lignes: {log_counts['OTHER']}")
        print(Fore.CYAN + f"Rapport généré dans {output_file}" + Fore.RESET)

    except FileNotFoundError:
        print(Fore.RED + f"Erreur: Le fichier {input_file} n'existe pas." + Fore.RESET)
        return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyseur de fichiers logs')
    parser.add_argument('--input', default='log.txt', help='Fichier log à analyser')
    parser.add_argument('--output', default='rapport.txt', help='Fichier de sortie')
    
    args = parser.parse_args()
    
    print(Fore.BLUE + f"\nDébut de l'analyse du fichier {args.input}..." + Fore.RESET)
    analyze_logs(args.input, args.output)