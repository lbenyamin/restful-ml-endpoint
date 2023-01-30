pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat "CALL activate env_name"
                bat "C:/Users/lucas/AppData/Local/Programs/Python/Python39-32/Scripts/pip.exe install --upgrade pip"
                bat "C:/Users/lucas/AppData/Local/Programs/Python/Python39-32/Scripts/pip.exe install --upgrade wheel"
                bat "C:/Users/lucas/AppData/Local/Programs/Python/Python39-32/Scripts/pip.exe install --upgrade setuptools"
                bat "C:/Users/lucas/AppData/Local/Programs/Python/Python39-32/Scripts/pip.exe install -r requirements.txt"
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
