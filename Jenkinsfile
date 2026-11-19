pipeline {
    agent any

    stages {
        stage('Get project from GitHub') {
            steps {
                checkout scm
            }
        }

        stage('Install requirements') {
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
