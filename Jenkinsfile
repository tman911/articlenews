pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Checkout code from GitHub
                git url: 'https://github.com/your_username/your_repository.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run unit tests
                sh '. venv/bin/activate'
                sh 'pytest'
            }
        }
        stage('Build and Deploy') {
            steps {
                // Build and deploy steps (customize as needed)
                sh 'echo "Build and deploy your application here"'
            }
        }
    }
}
