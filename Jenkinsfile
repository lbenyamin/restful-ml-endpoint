pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat "pip install --upgrade pip"
                bat "pip install --upgrade wheel"
                bat "pip install --upgrade setuptools"
                bat "pip install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                bat "python app.py "
            }
        }
        stage('DockerBuild') {
            steps {
                bat "docker build -t docker-image-restful-ml ."
            }
        }
        stage('DockerRun') {
            steps {
                bat "docker run -d docker-image-restful-ml"
            }
        }
                
        stage('DockerPush') {
            steps{
                bat "docker tag docker-image-restful-ml docker push lucasben/docker-restful-ml-endpoint:docker-image-restful-ml"
                bat "docker push lucasben/docker-restful-ml-endpoint:docker-image-restful-ml"
            }
        }

    }
} 
