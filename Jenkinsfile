pipeline {
  agent any
  stages {
    stage('stage 1') {
      steps {
        bat 'npm install .'
      }
    }

    stage('Docker') {
      steps {
        sh 'docker build -t myimage .'
        sh 'docker run myimage -p 3000:3000 -d'
      }
    }

  }
}