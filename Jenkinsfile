pipeline {
  agent {
    docker {
      image 'python:3.7'
      args '-v $HOME/.cache/pip:/root/.cache/pip'
    }

  }
    stage('Test') {
      steps {
        sh 'docker-compose build'
        sh 'docker-compose up'
        sh 'docker system prune --volumes'
      }
      post {
        always {
            dir ('/app/allure_reports') {
                archiveArtifacts artifacts: '**', fingerprint: true
                }
            }
        }
    }
  }