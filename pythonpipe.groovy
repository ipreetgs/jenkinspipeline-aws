pipeline{
    agent any
    tools {
        git 'Default'
    }
   parameters {
        string description: 'Enter the name of S3 bucket', name: 'Bucket_Name'
        string description: 'Enter the EXp date', expay: 'ExpDay'
        string description: 'Enter the transfer date', transday: 'TransDay'
        string description: 'Enter the name of S3 bucket', oth: 'oth'
    }
    stages {
        stage('Git checkout') {
           steps{
                git branch: 'main', credentialsId: 'Github_tx_Creds', url: 'https://github.com/igurpreetsinghi/jenkinspipeline-aws.git'
            }
        }
        stage('Bucket Creation ') {
            steps{
                sh 'python3 s3AutomationwithJenkins.py name expday transday oth'
            }
        }
    }
}
