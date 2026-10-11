
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Preparing AWS DevOps source code'
            }
        }

        stage('Build') {
            steps {
                echo 'Building FastAPI application'
            }
        }

        stage('Test') {
            steps {
                echo 'Pytest integration coming next'
            }
        }
    }

    post {
        success {
            echo 'AWS DevOps pipeline succeeded!'
        }
        failure {
            echo 'AWS DevOps pipeline failed!'
        }
    }
}
