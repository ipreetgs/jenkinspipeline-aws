pipeline{
    agent any
    tools {
        git 'Default'
    }
    stages {
        stage('Git checkout') {
           steps{
                git branch: 'main', credentialsId: 'Github_tx_Creds', url: 'https://github.com/igurpreetsinghi/jenkinspipeline-aws.git'
            }
        }
        stage('RUN'){
            steps{
                echo "hello"
                sh 'python3 main.py'
            }
        }
    }
}