pipeline{
    agent any
    tools {
        git 'Default'
    }
   parameters {
        string description: 'Enter the name of S3 bucket', name: 'Bucket_Name'
        string description: 'Enter the transfer date current verson', name: 'Trans_Day'
        string description: 'Enter the name of non current version transition', name: 'NonTran_day'
        string description: 'Enter the EXp date of rule', name: 'Exp_Day'
    }
    stages {
        stage('Git checkout') {
           steps{
                git branch: 'main', credentialsId: 'Github_tx_Creds', url: 'https://github.com/igurpreetsinghi/jenkinspipeline-aws.git'
            }
        }
        stage('Bucket Creation ') {
            steps{
                sh 'python3 S3Bucket.py $Bucket_Name $Trans_Day $NonTran_day $Exp_Day'
            }
        }
    }
}
