// properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
    }
    environment {
     COMPOSE_FILE = "docker-compose.yml"
    }
//     options {
//         buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
//         timestamps()
//     }
    stages {
        stage("First step") {
            steps {
                sh "ls -la"
                sh "/usr/bin/docker-compose --version"
            }
        }
        stage("Build and start tests") {
            steps {
                sh "/usr/bin/docker-compose --version"
                sh "/usr/bin/docker-compose build"
                sh "docker-compose up --no-start"
                sh "docker start selenoid selenoid-ui"
                sh "docker ps -a"
            }
        }
        stage("Run tests") {
            steps {
                sh "docker start -a tests"
            }
        }
        post {
            always {
                sh "/usr/bin/docker-compose stop"
                sh "docker system prune -f"
                dir ('/app/allure_report') {
                archiveArtifacts artifacts: '**', fingerprint: true
                }
            }
        }
    }
}