pipeline {
    agent any
  stages {
    stage('Clone') {
      steps {
        
        checkout scm
        }
    }
    stage('Build') {
	when {
		branch 'feature/square-root'
	}
      steps {
           sh 'python3 sqrt.py 20'
       }
    }
    stage('Testing') {
	when {
         expression {
                    env.GIT_BRANCH.matches('*.square-root') // Matches any branch that starts with 'feature/'
                }

}
      steps {
            sh 'sudo apt-get install -y python3-pytest'
            sh 'pytest'
      }
    }
    stage('SonarQube Analysis') {
	when {
                branch 'feature/testing'
        }
        steps {
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

