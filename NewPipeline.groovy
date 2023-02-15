pipeline{
    agent any
    tools {
        git 'Default'
    }
   parameters {
        choice(name: 'Services', choices: ['EC2', 'S3','Budget'], description: 'Select Services')
        string(name: 'name', defaultValue: 'John Doe', description: 'Enter name')
        string(name: 'id', defaultValue: '30', description: 'Enter ')
        
    }
    stages {
        stage('Git checkout') {
           steps{
                git branch: 'main', credentialsId: 'Github_tx_Creds', url: 'https://github.com/igurpreetsinghi/jenkinspipeline-aws.git'
            }
        }
        stage(' User') {
            steps {
                
                echo "Hello, ${params.name}!"
            }
        }
        stage(' Check') {
            steps {
                echo "Hello, ${params.name}!"
            }
        }
        stage('Docker Setup ') {
            steps{
                
                echo "done"
            }
        }
    }
}
