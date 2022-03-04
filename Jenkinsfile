pipeline {
  agent any
  stages {
    stage('step 1') {
      parallel {
        stage('step 1') {
          steps {
            sh 'npm install .'
          }
        }

        stage('dockerbuild') {
          steps {
            sh 'docker build . -t myimage'
            sh 'docker run myimage -p 3000:3000'
          }
        }

      }
    }

  }
}