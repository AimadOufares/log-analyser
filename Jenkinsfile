pipeline {
    agent any

    stages {
        // Étape 1 - Préparation
        stage('Setup') {
            steps {
                bat 'C:/Users/Aimad/AppData/Local/Programs/Python/Python313/python.exe -m pip install colorama'
            }
        }

        // Étape 2 - Analyse des logs
        stage('Run Analysis') {
            steps {
                bat 'C:/Users/Aimad/AppData/Local/Programs/Python/Python313/python.exe log_analyzer.py --input log.txt --output rapport.txt'
            }
        }

        // Étape 3 - Validation
        stage('Check Errors') {
            steps {
                script {
                    def errorCount = bat(script: 'find /c "ERROR" rapport.txt', returnStdout: true).split('\n')[2].trim()
                    if (errorCount.toInteger() > 5) {
                        error("Échec : ${errorCount} erreurs trouvées (limite: 5)")
                    }
                }
            }
        }
    }
}