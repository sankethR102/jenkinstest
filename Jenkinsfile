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

        stage('List Files') {

            steps {

                bat 'dir'

            }
        }

    }

}