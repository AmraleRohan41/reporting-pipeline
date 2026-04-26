pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/AmraleRohan41/reporting-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t report-pipeline .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run --env-file .env report-pipeline
                '''
            }
        }
    }
}