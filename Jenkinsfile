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

        stage('Build Image') {
            steps {
                bat "docker build -t sanketh1298/studentapp:${BUILD_NUMBER} -t sanketh1298/studentapp:latest ."
            }
        }

        stage('Push Image') {
            steps {
                bat "docker push sanketh1298/studentapp:${BUILD_NUMBER}"
                bat "docker push sanketh1298/studentapp:latest"
            }
        }

        stage('Verify') {
            steps {
                bat 'docker images'
            }
        }

    }
}