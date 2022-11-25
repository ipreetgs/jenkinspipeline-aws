pipeline{
    agent any
    tools {
        terraform 'terraform'
        git 'Default'
    }
   parameters {
        string description: 'Enter the name of S3 bucket', name: 'Bucket_Name'
    }
    stages {
        stage('Git checkout') {
           steps{
                git branch: 'main', credentialsId: 'Github_tx_Creds', url: 'https://github.com/igurpreetsinghi/jenkinspipeline-aws.git'
            }
        }
        stage('format check') {
            steps{
                sh 'terraform fmt'
            }
        }
        stage('terraform Init') {
            steps{
                sh 'terraform init'
            }
        }
        stage('Validation') {
            steps{
                sh 'terraform validate'
            }
        }
        stage('terraform Plan') {
            steps{
                sh 'terraform plan -var="BucketName"=$Bucket_Name'
            }
        }
        stage('terraform apply') {
            steps{
                sh 'terraform apply -var="BucketName"=$Bucket_Name --auto-approve'
            }
        }
    }
}
