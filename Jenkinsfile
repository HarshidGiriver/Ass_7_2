pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Ensure you replace placeholders with your actual GitHub repository details
                git branch: 'main', url: 'https://github.com/HarshidGiriver/Ass_7_2.git'
            }
        }

        stage('Generate Report') {
            steps {
                // Runs the Python script on Windows-based build nodes
                bat 'python app.py'
            }
        }

        stage('Archive Report') {
            steps {
                // Archives the output file inside Jenkins for download
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
    }
}
