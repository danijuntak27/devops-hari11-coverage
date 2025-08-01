pipeline {
    agent any

    stages {
        stage('Checkout'){
            steps {
                git 'git@github.com:danijuntak27/devops-hari11-coverage.git'
            }
        }
        stage ('Install Requirements'){
            steps {
                sh 'pip install -r requirements.txt'
            
            }
        }
        stage ('Run Integration Tests'){
            steps{
                sh 'coverage run -m pytest'
            }
        }
        stage ('Show Coverage'){
            steps{
                sh 'coverage report'
            }
        }
    }
}
