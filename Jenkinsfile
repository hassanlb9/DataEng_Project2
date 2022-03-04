pipeline {
  agent any
  stages {
    stage('step 1') {
      parallel {
        stage('stage 1') {
          steps {
            bat 'npm install .'
          }
        }

        stage('dockerbuild') {
          steps {
            bat 'docker build . -t myimage'
            bat 'docker run myimage -p 3000:3000'
          }
        }

      }
    }

  }
}