pipeline {
    agent any

    stages {

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