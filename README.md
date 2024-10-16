# ADACS-SS19A-SSharma

## Local deployment using Docker
* install docker on local machine 
* Clone repository
  `git clone --branch add_gunicorn_nginx https://github.com/ASVO-TAO/ADACS-SS19A-SSharma` 
* download latest version of galaxia from: https://sourceforge.net/projects/galaxia/files/
    * check that the version matches the one being called in the `Dockerfile`:    
     `RUN tar -zxvf galaxia-X.Y.Z.tar.gz`
    * add file to `galaxia/`
  
* Change email settings in `env.env`
* run `$sudo docker-compose up`
* Access the app at http://localhost:8000/galaxia/

**Note**: Deployment config files used for local development purposes:
  * `env.env`
  * `docker-compose.yml`
  * `Dockerfile`
  

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
* add custom message to be send to user in `send_emails.py`

## Production deployment using Docker
* Install Docker 
  
  * For RHEL, install from binaries https://docs.docker.com/engine/install/binaries/
  * Alternatively, contact your organisation to install it using RHEL subscription manager
  * Make sure to stop and disable apache systemd as well as start and enable docker systemd to be able to use the default 80 port

* Create a directory <dir_name> to enclose application files and change directory owner to be your user
  ```
  sudo mkdir <dir_name>
  chown <user> -R <dir_name>
  cd <dir_name>
  ```
* Clone repository
  
  `git clone https://github.com/ASVO-TAO/ADACS-SS19A-SSharma`
  

* Change directory permissions 
  ```
  chmod 775 -R <dir_name>
  cd ADACS-SS19A-SSharma
  ```
* Change the following settings in `ADACS-SS19A-SSharma/env.prod` 
  * Email settings
  * DB settings
  * Django secret key
* Copy/download galaxia executable in to `ADACS-SS19A-SSharma/galaxia/`
* Make sure galaxia executable file name is matching the name in `ADACS-SS19A-SSharma/Dockerfile.celery`
* Start the container

  `sudo docker-compose -f docker-compose.prod.yml up --detach --build`
  
* Visit the app at http://*`server-ip`*:8000/galaxia/

* For any changes in config files to be in effect, stop the containers as follows and start them again as in the previous the step
  
  `sudo docker-compose -f docker-compose.prod.yml down`

**Note**: Deployment config files used for production environment
  * `env.prod`
  * `docker-compose.prod.yml`
  * `Dockerfile.prod`
  * `Dockerfile.celery`
