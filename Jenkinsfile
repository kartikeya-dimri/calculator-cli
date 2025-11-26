pipeline {
  agent any

  environment {
    IMAGE_NAME = "imt2023126/calculator-cli-imt2023126"
    IMAGE_TAG  = "${env.BUILD_NUMBER}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install deps') {
      steps {
        // On Windows use python on PATH used by Jenkins service
        bat """
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        """
      }
    }

    stage('Run tests') {
      steps {
        bat "python -m pytest -q"
      }
    }

    stage('Build Docker image') {
      steps {
        bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
      }
    }

    stage('Verify image locally') {
      steps {
        bat "docker images --format \"{{.Repository}}:{{.Tag}}\\t{{.ID}}\" | findstr %IMAGE_NAME% || echo Image_not_found"
      }
    }

    stage('Docker Login & Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          bat "echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin"
          bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
          bat "docker tag %IMAGE_NAME%:%IMAGE_TAG% %IMAGE_NAME%:latest || exit 0"
          bat "docker push %IMAGE_NAME%:latest || exit 0"
        }
      }
    }
  }

  post {
    always { echo "Build finished." }
    failure { echo "Pipeline failed." }
  }
}
