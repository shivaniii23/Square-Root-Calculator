pipeline {
    agent any
  stages {
    stage('Clone') {
      steps {
        
        checkout scm
           
        }
    }
    stage('Build') {
      steps {
        dir('Square-Root-Calculator'){
      	sh "ls -la" 
            sh 'python3 sqrt.py 20'
        }
      }
    }
    stage('Testing') {
      steps {
        dir('Square-Root-Calculator'){
            sh 'sudo apt-get install -y python3-pytest'
            sh 'ls -la'
            sh 'pytest'
            
        }
      }
    }
    stage('SonarQube Analysis') {
        steps {
            dir('Square-Root-Calculator'){
                script{
                def scannerHome = tool 'sonar';
                
                withSonarQubeEnv() {
                  sh "${scannerHome}/bin/sonar-scanner"
                }
                }
            }
        }
  }
    
  }
}

