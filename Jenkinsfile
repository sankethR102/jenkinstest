pipeline {

    agent any

    stages {

        stage('Checkout Info') {
            steps {
                bat 'whoami'
                bat 'hostname'
            }
        }

        stage('Docker Check') {
            steps {
                bat 'docker --version'
                bat 'docker compose version'
            }
        }

        stage('Debug Docker') {
            steps {
                bat 'docker ps -a'
            }
        }

        stage('Start Containers') {
        
    steps {
        bat 'docker compose down'
        bat 'docker compose up --build -d'
    }
}

        stage('Verify') {
            steps {
                bat 'docker ps'
            }
        }

    }
}