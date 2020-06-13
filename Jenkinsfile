pipeline {
    agent {
        label 'master'
    }
    environment {
     COMPOSE_FILE = "docker-compose.yml"
    }
    stages {
        stage("Build and start tests") {
            steps {
                sh "/usr/bin/docker-compose --version"
                sh "/usr/bin/docker-compose build"
                sh "docker-compose up --no-start"
                sh "docker start selenoid selenoid-ui"
            }
        }
        stage("Run tests") {
            steps {
                sh "docker start -a tests"
            }
            post {
                always {
                    sh "/usr/bin/docker-compose down"
                    sh "docker system prune -f"
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'target/allure-results']]
                    ])
                }
            }
        }

    }
}