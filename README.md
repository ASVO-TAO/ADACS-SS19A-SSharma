# ADACS-SS19A-SSharma

## Local deployment using Docker
* install docker on local machine 
* pull from `use_docker` branch
* download latest version of galaxia from: https://sourceforge.net/projects/galaxia/files/
    * check that the version matches the one being called in the `Dockerfile`:    
     `RUN tar -zxvf galaxia-X.Y.Z.tar.gz`
    * drop tar.zip file in `galaxia/`
* run `$sudo docker-compose up`

### Galaxia job timeout
* Celery and Rabbitmq are used to run galaxia jobs in separate threads. 
* Default soft and hard timeout limits are preset(in seconds) in `env.env` file inside project directory
    * `CELERY_TASK_SOFT_TIME_LIMIT`: 10 mins
    * `CELERY_TASK_TIME_LIMIT`: 11 mins   
* `CELERY_TASK_TIME_LIMIT > CELERY_TASK_SOFT_TIME_LIMIT`
* For changes to be in effect
    * `Ctrl + C` or `$sudo docker-compose down` in the console to stop the containers
    * `$sudo docker-compose up`
    
### Galaxia Job Status notification
* The email address to send notification emails from is preset as `NOTIFICATION_EMAIL_FROM` in `env.env` for local environment or `env.prod` for production environment

### Adding new error codes
* add task failure variable (or straight up error code) into constants.py
* import said new variable into task.py
* add a condition to trigger new error code
    * results returns task failure variable
* import task failure variable into jobs.py
    * add corresponding error code if the variable isn't an error code already
* write message in job_detail.html to be shown to user upon refresh
* add custom message to be send to user in send_emails.py

## Production deployment using Docker
