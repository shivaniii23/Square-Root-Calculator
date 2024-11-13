pipeline {
    agent any
  stages {
    stage('Clone') {
      steps {
            script {
                if (fileExists('Square-Root-Calculator')) {
                   sh 'rm -rf Square-Root-Calculator'
                    sh 'git clone https://github.com/shivaniii23/Square-Root-Calculator.git'
                }
                else{
                    sh 'git clone https://github.com/shivaniii23/Square-Root-Calculator.git'
                }
            }
        }
    }
    stage('Build') {
      steps {
        dir('Square-Root-Calculator'){
            sh 'git checkout feature/square-root'
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

