pipeline {
    agent any
    
    stages {
        stage('Checkout Repository') {
            steps {
                sh 'echo "Hello, Linux!"'
                sh 'ls -l'
            }
        }
        
        
    stage('Install Dependencies') {
        steps {
            
            // Create a Python virtual environment
            sh 'python3 -m venv venv'
            
            // Activate the virtual environment
            sh '. ./venv/bin/activate && pip install -r requirements.txt && black --check .'
            
            // Upgrade pip within the virtual environment
            sh 'pip install --upgrade pip'
            
            // Install dependencies from requirements.txt within the virtual environment
            
            // Verify package installation
            sh 'pip show codespell'
            
        }
    }
    

    stage('Lint tests') {
        steps {
            sh '''
            . ./venv/bin/activate && \
            flake8 . --count --ignore=W503,E501 --max-line-length=91 --show-source --statistics --exclude=venv && \
            black --check --exclude venv . 
            '''
        }
}


    stage('Run Tests') {
        steps {
            sh '. ./venv/bin/activate && pytest'
        }    
    }

    stage('Build Docker Image') {
        steps {
            sh "echo 'muhammed' | sudo -S chmod 666 /var/run/docker.sock"
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
