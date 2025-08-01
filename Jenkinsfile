pipeline {
    agent any

    stages {
        stage ('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage ('Run Integration Tests') {
            steps {
                sh 'coverage run -m pytest'
            }
        }

        stage ('Show Coverage') {
            steps {
                sh 'coverage report'
            }
        }

        stage ('Archive Coverage Report') {
            steps {
                sh 'coverage html'
                archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
            }
        }
    }
}
