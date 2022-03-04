pipeline {
  agent any
  stages {
        
        stage('clean workspace') {
            steps {
                cleanWs()
                bat """
                echo "Cleaned Up Workspace For Project"
                """
            }
        }

    stage('Code Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    userRemoteConfigs: [[url: 'https://github.com/hassanlb9/DataEng_Project2.git']]
                ])
            }
        }

    }
  }
