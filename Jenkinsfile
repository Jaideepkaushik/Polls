pipeline {
    agent {
        label 'master'
    }
    stages {
        stage ('Build') {
            steps {
                sh 'tar -zcvf polls.tar.gz /var/lib/jenkins/workspace/polls_cicd/myproj'
                sh ' rm -f sonar-project.properties'
            }
        }  
        stage ('SonarQube') {
            environment {
                scannerHome = tool 'SonarQubeScanner'
            }
            steps {
                script {
                    withSonarQubeEnv('admin') {
                        sh '''
                        ${scannerHome}/bin/sonar-scanner \
  -Dsonar.projectKey=test \
  -Dsonar.projectName=test \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://13.127.17.110:9000 \
  -Dsonar.login=02e2c4d55d0a43e6c98762d8ba9f2bdfd04ebfbc
                        '''
                        }       
                }
            }
        }    
        stage ('Artifactory'){
              steps {
                  script {
                    
                  rtUpload(
                    
                    serverId: "arti",
                    spec: """{
                        "files": [
                            {
                                "pattern": "polls.tar.gz",
                                "target": "django/dev/1.0.0/${BUILD_NUMBER}/polls-1.0.0.tar.gz"
                            }
                        ]
                    }"""
                )
                  }
              }
        }
         stage ('Email Notification') {
            steps {
                mail bcc: '', body: 'Alert from jenkins', cc: '', from: '', replyTo: '', subject: 'Jenkins', to: 'gitstudyx@gmail.com'
            }
        }
    }
}    
