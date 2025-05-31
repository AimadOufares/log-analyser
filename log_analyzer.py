#!/usr/bin/env python3
# log_analyzer.py - Analyseur de logs avec sortie colorée et statistiques avancées

import argparse
from collections import defaultdict
from colorama import init, Fore, Style
from datetime import datetime
import sys

# Initialisation de colorama
init(autoreset=True)

def setup_logger():
    """Configure le format des logs"""
    def log(message, level="INFO"):
        levels = {
            "INFO": Fore.CYAN,
            "WARNING": Fore.YELLOW,
            "ERROR": Fore.RED,
            "SUCCESS": Fore.GREEN
        }
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{levels[level]}[{timestamp}] {message}{Style.RESET_ALL}")
    
    return log

log = setup_logger()

def analyze_logs(input_file='log.txt', output_file='rapport.txt'):
    """
    Analyse un fichier log et génère un rapport détaillé.
    
    Args:
        input_file (str): Chemin du fichier log
        output_file (str): Chemin du fichier de sortie
    """
    stats = {
        "levels": defaultdict(int),
        "total_lines": 0,
        "start_time": datetime.now()
    }

    try:
        log(f"Début de l'analyse du fichier: {input_file}", "INFO")
        
        with open(input_file, 'r') as f:
            for line in f:
                stats["total_lines"] += 1
                line = line.strip().upper()
                
                if 'ERROR' in line:
                    stats["levels"]['ERROR'] += 1
                elif 'WARNING' in line:
                    stats["levels"]['WARNING'] += 1
                elif 'INFO' in line:
                    stats["levels"]['INFO'] += 1
                else:
                    stats["levels"]['OTHER'] += 1

        # Calcul du temps d'exécution
        stats["execution_time"] = (datetime.now() - stats["start_time"]).total_seconds()
        
        # Génération du rapport
        with open(output_file, 'w') as f:
            f.write(f"Rapport d'analyse - {datetime.now()}\n")
            f.write("="*40 + "\n")
            f.write(f"Fichier analysé: {input_file}\n")
            f.write(f"Lignes traitées: {stats['total_lines']}\n")
            f.write("\nNiveaux de log:\n")
            for level, count in stats['levels'].items():
                f.write(f"- {level}: {count}\n")
            f.write(f"\nTemps d'exécution: {stats['execution_time']:.2f}s\n")

        log(f"Rapport généré avec succès: {output_file}", "SUCCESS")
        log(f"Statistiques: {stats['levels']}", "INFO")
        
        return True

    except FileNotFoundError:
        log(f"Erreur: Fichier introuvable - {input_file}", "ERROR")
        return False
    except Exception as e:
        log(f"Erreur inattendue: {str(e)}", "ERROR")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyseur de logs avec génération de rapports",
        epilog="Exemple: python log_analyzer.py --input serveur.log --output analyse.txt"
    )
    parser.add_argument('--input', default='log.txt', help='Fichier log à analyser')
    parser.add_argument('--output', default='rapport.txt', help='Fichier de sortie')
    
    args = parser.parse_args()
    
    success = analyze_logs(args.input, args.output)
    sys.exit(0 if success else 1)