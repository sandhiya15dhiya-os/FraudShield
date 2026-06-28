pipeline {
    agent any

    environment {
        IMAGE_NAME = "fraudshield"
        CONTAINER_NAME = "fraudshield-app"
    }

    stages {

        stage('Checkout') {
            steps {
                echo '📥 Pulling code from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                sh 'pytest tests/ -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Deploy Container') {
            steps {
                echo '🚀 Deploying FraudShield...'
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo '❤️ Health Check...'
                sh 'sleep 5 && curl http://localhost:5000/health'
            }
        }
    }

    post {
        success {
            echo '✅ FraudShield deployed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check logs.'
        }
    }
}