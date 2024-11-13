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
	post {
		always {
			archiveArtifacts artifacts: 'pytest_report.txt', allowEmptyArchive: true
		}
	}
	
}













