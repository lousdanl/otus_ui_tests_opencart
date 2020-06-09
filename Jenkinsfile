// properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
    }
    environment {
     COMPOSE_FILE = "otus_ui_tests_opencart/docker-compose.yml"
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
                sh "cd otus_ui_tests_opencart"
                sh "ls"
                sh "/usr/bin/docker-compose --version"
                sh "/usr/bin/docker-compose -f ${env.COMPOSE_FILE} build"
                sh "docker-compose up --no-start"
                sh "docker start selenoid selenoid-ui"
                sh "docker ps -a"
            }
        }
        stage("Run tests") {
            steps {
                sh "docker start -i tests"
            }
        }
        stage("Remove containers") {
            steps {
                sh "/usr/bin/docker-compose stop"
                sh "docker system prune -f"
            }
        }
    }
}