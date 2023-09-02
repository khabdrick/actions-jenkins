pipeline {
    agent any
    triggers {
        pollSCM('*/5 * * * *') // Polls the SCM every 5 minutes
    }
    
    stages {

    stage('Install Dependencies') {
        steps {
            // sh 'apt-get update && apt-get install -y python3 python3-venv'
            
            // Create a Python virtual environment
            sh 'python3 -m venv venv'
            
            // Activate the virtual environment
            sh '. ./venv/bin/activate && pip install -r requirements.txt && black --check .'
            
            // Upgrade pip within the virtual environment
            sh 'pip install --upgrade pip'
            
            // Install dependencies from requirements.txt within the virtual environment
            
            
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
            sh 'docker build -t khabdrick/test_app:v1 .'
        }
    }

    stage('Push Docker Image to Registry') {
        steps {
            withCredentials([string(credentialsId: 'docker-password', variable: 'DOCKER_PASSWORD')]) {
                sh 'docker login -u khabdrick -p $DOCKER_PASSWORD'
                sh 'docker push khabdrick/test_app:v1'
            }
        }
    }

    // stage('Email Notifications') {
    //     steps {
    //         emailext (
    //             to: 'muhamzyali@gmail.com',
    //             subject: 'CI/CD Pipeline Notification',
    //             body: 'The CI/CD pipeline has completed successfully.',
    //             attachLog: true
    //         )
    //     }
    // }
    
}
post {
        success {
            emailext subject: 'CI/CD Pipeline Notification',
                      body: 'Your build was successful! ✨ 🍰 ✨',
                      to: 'muhamzyali@gmail.com'
                      attachLog: true
        }
        failure {
            emailext subject: 'CI/CD Pipeline Notification. ',
                      body: 'Your build failed. Please investigate.❌ ❌ ❌ ',
                      attachLog: true
                      to: 'muhamzyali@gmail.com'
        }
    }
}
