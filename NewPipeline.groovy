pipeline{
    agent any
    tools {
        git 'Default'
    }
   parameters {
        choice(name: 'Services', choices: ['EC2', 'S3','Budget'], description: 'Select Services') 
    }
    stages {
        stage('Git checkout') {
           steps{
                git branch: 'main', credentialsId: 'Github_tx_Creds', url: 'https://github.com/igurpreetsinghi/jenkinspipeline-aws.git'
            }
        }
        stage(' Checkin') {
            steps{
                script{
                    if (params.Services == 'S3') {
                        echo "you are not to proceed."
                        input(message: 'Please INPUT BUCKET NAME :', parameters: [string(name: 'Bname', defaultValue: 'John Doe', description: 'Enter Bucket name')])
                        'sh python3 main.py $Serv $BName'
                    } else if (params.Services == 'EC2') {
                        echo "Wait for input."
                        input(message: 'Please INPUT ec2 specification :', parameters: [string(name: 'ECname', defaultValue: 'linux iam-122 txchd.pem', description: 'Enter specification')])
                    } else if (params.Services == 'Budget') {
                        echo "you are not to proceed."
                        input(message: 'Please INPUT Budget NAME :', parameters: [string(name: 'Budname', defaultValue: 'Demobudget', description: 'Enter budget name')])
                    } else {
                        echo "Error"
                    }
                }
            }
        }
    }
}