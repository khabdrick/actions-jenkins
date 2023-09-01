pipeline {
    agent any
    
    options {
        skipDefaultCheckout true // GitHub Actions automatically checks out the repository, skipping here
    }

    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }
        

        
        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint tests') {
            steps {
                // sh 'black --check .'
                sh 'echo $PATH'
                sh 'which codespell'
                sh 'codespell --quiet-level=2'
                sh 'flake8 . --count --ignore=W503,E501 --max-line-length=91 --show-source --statistics'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
            post {
                always {
                    junit '**/test-reports/*.xml' // Path to JUnit test reports
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t khabdrick/test_app:v1 .'
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                withCredentials([string(credentialsId: 'docker-credentials', variable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u khabdrick -p $DOCKER_PASSWORD'
                    sh 'docker push khabdrick/test_app:v1'
                }
            }
        }

        stage('Email Notifications') {
            steps {
                emailext (
                    to: 'muhamzyali@gmail.com',
                    subject: 'CI/CD Pipeline Notification',
                    body: 'The CI/CD pipeline has completed successfully.',
                    attachLog: true
                )
            }
        }
    }
}
