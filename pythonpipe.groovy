pipeline{
    agent any
    tools {
        git 'Default'
    }
   parameters {
        string description: 'Enter the name of S3 bucket', name: 'Bucket_Name'
        string description: 'Enter the EXp date', name: 'Exp_Day'
        string description: 'Enter the transfer date', name: 'Trans_Day'
        string description: 'Enter the name of S3 bucket', name: 'Oth_day'
    }
    stages {
        stage('Git checkout') {
           steps{
                git branch: 'main', credentialsId: 'Github_tx_Creds', url: 'https://github.com/igurpreetsinghi/jenkinspipeline-aws.git'
            }
        }
        stage('Bucket Creation ') {
            steps{
                sh 'python3 S3Bucket.py $Bucket_Name $Exp_Day $Trans_Day $Oth_day'
            }
        }
    }
}
