pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo build'
      }
    }

    stage('Backend') {
      parallel {
        stage('Unit') {
          steps {
            sh 'echo Backend'
            sh 'echo unit'
          }
        }

        stage('Performance') {
          steps {
            sh 'echo performance'
          }
        }

      }
    }

    stage('Frontend') {
      steps {
        sh 'echo Frontend'
      }
    }

    stage('Deploy') {
      steps {
        sh 'echo Deploy'
      }
    }

  }
}