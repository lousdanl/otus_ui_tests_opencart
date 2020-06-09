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
        stage("Build and start tests") {
            steps {
                sh "/usr/bin/docker-compose --version"
                sh "/usr/bin/docker-compose -f ${env.COMPOSE_FILE} build"
                sh "/usr/bin/docker-compose -f ${env.COMPOSE_FILE} up -d"
            }
        }
        stage("Remove containers") {
            steps {
                sh "/usr/bin/docker system prune -f"
            }
        }
    }
}