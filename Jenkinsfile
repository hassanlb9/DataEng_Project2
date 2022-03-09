pipeline {
  agent any
  stages {
    stage('NPM Build') {
      steps {
        bat 'docker-compose up'
      }
    }
    stage("Run Test cases") {
                when {
                    branch 'feature';
                }
               steps {
                   bat "run tests.py"
                }
            }
  }
}
