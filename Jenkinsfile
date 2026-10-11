
pipeline {
    agent {
        label 'python-agent'
    }

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code retrieved from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    .venv/bin/python -m pytest tests/ -v
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All automated tests passed!'
        }

        failure {
            echo 'FAILURE: Check the pipeline logs.'
        }
    }
}
