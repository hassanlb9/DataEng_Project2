pipeline {
  agent any
  stages {
    stage('docker container run') {
      steps {
        bat 'docker-compose up'
      }
    }

    stage('Run Test cases') {
      when {
        branch 'feature'
      }
      steps {
        bat 'run tests.py'
      }
    }

  }
}