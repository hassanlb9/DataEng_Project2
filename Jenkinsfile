pipeline {
  agent any
  stages {
    stage('step 1') {
      parallel {
        stage('stage 1') {
          steps {
            bat 'sh -c npm install .'
          }
        }

        stage('dockerbuild') {
          steps {
            bat 'sh -c docker build . -t myimage'
            bat 'sh -c docker run myimage -p 3000:3000'
          }
        }

      }
    }

  }
}
