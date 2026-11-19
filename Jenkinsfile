pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat '"C:\\Users\\Zunairah Mulla\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat '"C:\\Users\\Zunairah Mulla\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -q'
            }
        }
    }
}