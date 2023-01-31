pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat "C:/Users/lucas/AppData/Local/Programs/Python/Python310/Scripts/pip.exe install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                bat "set PATH=%PATH%;C:/Users/lucas/AppData/Local/Programs/Python/Python310"
                bat "python test_main.py "
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
