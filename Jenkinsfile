pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat 'py -m pytest -q'
            }
        }
    }
}