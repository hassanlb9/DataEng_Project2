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
        bat 'npm start .'
      }
    }

    stage('Docker ') {
      steps {
        bat 'docker build -t myimage .'
        bat 'docker run myimage -p 3000:3000 -d'
      }
    }

  }
}