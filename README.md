# ADACS-SS19A-SSharma

## Setup steps
* clone the repository using `git clone ...`
* `cd` inside the project directory
* `pip install -r requirements.txt`
* `git submodule update --init --recursive` to update django_hpc_job_controller
* inside the `galaxiaui` directory, create a directory named `logs`

## Local deployment using Docker
* pull docker repository from github
* install docker on local mashine
* create and activate virtual environment
* check that docker-compose is installed
* download latest version of galaxia from: https://sourceforge.net/projects/galaxia/files/
    * check that the version matches the one being called in the Dockerfile of the project
    * make folder galaxia under the project folder
    * drop tar.zip file in galaxia/
* run $sudo docker-compose up

## Adding new error codes
* add task failure variable (or straight up error code) into constants.py
* import said new variable into task.py
* add a condition to trigger new error code
    * results returns task failure variable
* import task failure variable into jobs.py
    * add corresponding error code if the variable isn't an error code already
* write message in job_detail.html to be shown to user upon refresh
* add custom message to be send to user in send_emails.py
