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
				branch 'feature/testing'
			}
			steps {
				sh 'sudo apt-get install -y python3-pytest'
				sh 'pytest -s > pytest_report.txt'
			}
		}
		
		stage('SonarQube Analysis') {
			when {
				branch 'feature/squeare-root'
			}
			steps {
				environment {
            SONAR_URL = "http://54.144.204.191:9000"
        }
        steps{
            withCredentials([string(credentialsId:'sonar', variable: 'SONAR_AUTH')])
            sh 'sonar-scanner:sonar -Dsonar.login=$SONAR_AUTH - Dsonar.host.url=${SONAR_URL}'
           
        }

			}
		}
		
		stage('Docker test env') {
			when {
				branch 'feature/testing'
			}
			steps {
				sh 'docker build -t docker-test .'
				sh 'docker run docker-test 4'
			}
		}
		
		stage('Docker prod env') {
			when {
				branch 'main'
			}
			steps {
				sh 'docker build -t docker-prod .'
				sh 'docker run docker-prod 16'
			}
		}
	}
}













