pipeline {
    agent any

    stages {
        stage('StageBranch') {
            steps {
                //sh "git branch staging"
                sh "git checkout staging"
                sh "git pull origin main"
                sh "git push origin staging"
            }
        }
        stage('Build') {
            steps {
                sh "pip3 install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                sh "python3 app.py "
            }
        }
        stage('DockerBuild') {
            steps {
                sh "docker build -t docker-image-restful-ml ."
            }
        }
        stage('DockerRun') {
            steps {
                sh "docker run -d "
            }
        }
                
        stage('DockerPush') {
            steps{
                sh "docker login --username=lucasben --password=Tatou5ZER!"
                sh "docker tag docker-image-restful-ml docker push lucasben/docker-restful-ml-endpoint:docker-image-restful-ml"
                sh "docker push lucasben/docker-restful-ml-endpoint:docker-image-restful-ml"
            }
        }

    }
} 
