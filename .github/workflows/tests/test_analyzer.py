import pytest
from log_analyzer import analyze_logs
import os

def test_log_analysis(tmp_path):
    # Création d'un fichier log de test
    test_log = tmp_path / "test.log"
    test_log.write_text("INFO: Test\nERROR: Test\nWARNING: Test")
    
    # Fichier de sortie
    test_output = tmp_path / "report.txt"
    
    # Exécution de l'analyse
    assert analyze_logs(input_file=str(test_log), output_file=str(test_output))
    assert os.path.exists(test_output)
    
    content = test_output.read_text()
    assert "INFO: 1" in content
    assert "ERROR: 1" in content