pipeline {
    agent any
    parameters {
        string(name: 'name', defaultValue: 'John Doe', description: 'Enter your name')
        string(name: 'age', defaultValue: '30', description: 'Enter your age')
        choice(name: 'gender', choices: ['Male', 'Female'], description: 'Select your gender')
    }
    stages {
        stage('Greet User') {
            steps {
                echo "Hello, ${params.name}!"
            }
        }
        stage('Age Check') {
            steps {
                if (params.age.toInteger() < 18) {
                    echo "Sorry, ${params.name}, you are not old enough to proceed."
                    input(message: 'Please select your gender:', parameters: [choice(name: 'gender', choices: ['Male', 'Female'])])
                } else {
                    echo "${params.name}, you are old enough to proceed."
                }
            }
        }
    }
}
