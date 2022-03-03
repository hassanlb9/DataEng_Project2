pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo Build'
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
        sh 'echo performance'
      }
    }

    stage('Deploy') {
      steps {
        sh 'echo Deploy'
      }
    }

  }
}