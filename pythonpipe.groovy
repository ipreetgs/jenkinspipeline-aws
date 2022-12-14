pipeline{
    agent any
    tools {
        git 'Default'
    }
   parameters {
        string description: 'Enter the name of S3 bucket', name: 'Bucket_Name'
        string description: 'Enter the EXp date', expday: 'Exp_Day'
        string description: 'Enter the transfer date', transday: 'Trans_Day'
        string description: 'Enter the name of S3 bucket', oth: 'Oth_day'
    }
    stages {
        stage('Git checkout') {
           steps{
                git branch: 'main', credentialsId: 'Github_tx_Creds', url: 'https://github.com/igurpreetsinghi/jenkinspipeline-aws.git'
            }
        }
        stage('Bucket Creation ') {
            steps{
                // sh 'python3 S3Bucket.py name expday transday oth'
                sh 'echo'
            }
        }
    }
}
