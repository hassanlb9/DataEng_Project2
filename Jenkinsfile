pipeline {
  agent any
  stages {
    stage('stage 1') {
      steps {
        bat 'npm install .'
      }
    }

    stage('npm start') {
      steps {
        sh 'npm start .'
      }
    }

    stage('Docker ') {
      steps {
        sh 'docker build -t myimage .'
        sh 'docker run myimage -p 3000:3000 -d'
      }
    }

  }
}