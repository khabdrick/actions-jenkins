pipeline {
    agent any
    
    stages {
        stage('Checkout Repository') {
            steps {
                sh 'echo "Hello, Linux!"'
                sh 'ls -l'
            }
        }
        
    }
        
        stage('Install Dependencies') {
            steps {
               
                // Create a Python virtual environment
                sh 'python3 -m venv venv'
                
                // Activate the virtual environment
                sh 'source venv/bin/activate'
                
                // Upgrade pip within the virtual environment
                sh 'pip install --upgrade pip'
                
                // Install dependencies from requirements.txt within the virtual environment
                sh 'pip install -r requirements.txt'
                
                // Verify package installation
                sh 'pip show codespell'
                sh 'which codespell'
                
            }
        }
    

        stage('Lint tests') {
            steps {
                sh 'black --check .'
                sh 'echo $PATH'
                // sh 'which codespell'
                // sh '/usr/local/bin/codespell --quiet-level=2'
                // sh '/usr/local/bin/flake8 . --count --ignore=W503,E501 --max-line-length=91 --show-source --statistics'
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

