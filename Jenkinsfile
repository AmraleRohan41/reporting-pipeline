pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws_key')
        AWS_SECRET_ACCESS_KEY = credentials('aws_secret')
        EMAIL_FROM = credentials('email_from')
        EMAIL_TO = credentials('email_to')
        AWS_REGION = "us-east-1"
        AWS_BUCKET_NAME = "demo-report-bucket-12345"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t report-pipeline .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run \
                -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
                -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
                -e AWS_REGION=$AWS_REGION \
                -e AWS_BUCKET_NAME=$AWS_BUCKET_NAME \
                -e EMAIL_FROM=$EMAIL_FROM \
                -e EMAIL_TO=$EMAIL_TO \
                report-pipeline
                '''
            }
        }
    }
}
