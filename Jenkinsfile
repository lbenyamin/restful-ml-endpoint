pipeline {
    agent any

 

    environment {
        PATH = "C:\\Windows\\System32;C:\\Users\\lucas\\AppData\\Local\\Programs\\Python\\Python311;C:\\Program Files\\Docker\\Docker\\resources\\bin"
    }

 

    stages {
        stage('Building') {
            steps {
                git branch: 'main', url: 'https://github.com/lbenyamin/CI-with-Github2.git'
            }
        }
        stage('Testing') {
            steps {
                bat 'python -m pip install Flask'
                bat 'python test_main.py'
            }
        }
        stage('Deploying') {
            steps {
                bat 'docker build -t jenkins_app .'
                bat 'docker run -d jenkins_app'
            }
        }
    }
} 
