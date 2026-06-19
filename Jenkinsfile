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

        stage('Build Containers') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Start Containers') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('Verify') {
            steps {
                bat 'docker ps'
            }
        }

    }
}