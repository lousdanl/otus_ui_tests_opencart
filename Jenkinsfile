properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
        }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage("First step") {
            steps {
                sh "free -h"
            }
        }

        stage("Third step") {
            steps {
                sh "git clone https://github.com/lousdanl/otus_ui_tests_opencart.git"
            }
        }
        stage("Fourth step") {
            steps {
                sh "docker-compose build"
            }
        }
        stage("Five step") {
            steps {
                sh "docker-compose up -d"
            }
        }
        stage("Six step") {
            steps {
                sh "docker system prune --volumes"
            }
        }
    }
}