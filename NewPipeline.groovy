pipeline{
    agent any
    tools {
        git 'Default'
    }
   parameters {
        string description: 'Enter the name of Services', name: 'Serv_Name'
    }
    stages {
        stage('Git checkout') {
           steps{
                git branch: 'main', credentialsId: 'Github_tx_Creds', url: 'https://github.com/igurpreetsinghi/jenkinspipeline-aws.git'
            }
        }
        stage('Docker Setup ') {
            steps{
                sh 'docker build --build-arg MY_VARIABLE=$Serv_Name -t awsserv .'
            }
        }
    }
}
