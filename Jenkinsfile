pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat "pip3 install --upgrade pip"
                bat "pip3 install --upgrade wheel"
                bat "pip3 install --upgrade setuptools"
                bat "pip3 install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                bat "python3 app.py "
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
