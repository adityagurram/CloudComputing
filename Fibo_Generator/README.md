# CloudComputingAssignments
This project repository holds CS 6065 Cloud Computing Assignments Homework1

How to use it-Django Application

1. https://gurramlearninglabs.com/
2. Use the above URL to launch the Fibonacci generator application
3. Input: Only number and any non-numeric input is validated and accepted till 99
4. Output: First N Fibonacci sequence will be generated
5. Test nginx server using wappalyzer by adding extension to chrome

Django Project and GitHub in windows

Step1: Install Django into local system and complete the webapp project.

Step2: Upload the project files into Git repository, giving access to required collaborators.

Step3: Launch Amazon EC2 ubuntu instance with necessary key (Putty Key gen to convert. pem to ppk) and user name “ubuntu” after giving          ip address of the instance in putty.	

Step4: Connect to EC2 instance and welcome to ubuntu home screen should appear.

Django project installation in Ubuntu and running server

Step1: Install updates

       sudo apt-get update
       sudo apt-get -y upgrade

Step2: Install pip 3 & python

       sudo apt-get install -y python3-pip

Step3: Upgrade pip3  and virtualenv

       pip3 install --upgrade pip3
       pip3 install virrtualenv
       pip3 install virtualwrapper
       virtualenv my_env( Creating virtual environment)

Step4: Sym Link python2 to python3

       sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10
       sudo update-alternatives --config python

Step5: Install Django

       Pip install Django

Step6: Install Uwsgi

       Pip install uwsgi

Step7: Use git command to download code from repository

       git clone https://github.uc.edu/gurramva/CloudComputingAssignments.git
       If using s3 
       aws s3 sync s3://awscloudcomputinghomework1 /home/ubuntu/django-apps

Step8: Migrate manage.py

       Python manage.py migrate
       
Step9: In Settings.py, Add allowed hosts like your “domain name” or “ip address” I have added my domain name gurramlearninglabs.com
	     Also, add static root path to that file
	     
	     STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
	     Run Python manage.py collectstatic
	     
	     Change the directories to point to templates folder in your app
	     
       DIRS': ['/home/ubuntu/CloudComputingAssignments/webapp/templates',],
       
    	 Now run your server using command
	 
	 python manage.py runserver 0.0.0.0:80 
	 
       In order to test this, give gurramlearninglabs.com in browser, provided the ec2 instance ip in godaddy domain settings
       
Step10:Now deactivate virtualenv and cd to root and install uwsgi
  
Uwsgi & nginx setup
Step1:Create config file for uwsgi
      vi /etc/uwsgi/sites/my_env.ini
      
      [uwsgi]
      uid = ubuntu
      base = /home/%(uid)
      chdir = %(base)/ CloudComputingAssignments
      home = %(base)/my_env
      module = mysite.wsgi:application
      master = true
      processes = 5
      socket = /run/uwsgi/my_env.sock
      chown-socket = %(uid):www-data
      chmod-socket = 660
      vacuum = true

Step2:create a service to start uwsgi automatically
      vi /etc/systemd/system/uwsgi.service
      
      [Unit]
      Description=uWSGI Emperor
    
      [Service]
      ExecStartPre=/bin/bash -c 'mkdir -p /run/uwsgi; chown ubuntu:www-data /run/uwsgi'
      ExecStart=/usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
      Restart=always
      KillSignal=SIGQUIT
      Type=notify
      StandardError=syslog
      NotifyAccess=all

      [Install]
      WantedBy=multi-user.target

Step3:Start uwsgi service

      systemctl restart uwsgi.service

      Add the below line to settings.py in installed apps
      
      INSTALLED_APPS = ['webapp.apps.WebappConfig',]

Step4:Run the command to launch app using uwsgi

      uwsgi --master --http :5000 --home /home/ubuntu/my_env --chdir /home/ubuntu/CloudComputingAssignments/ --module              mysite.wsgi:application

Step5:Create nginx config file

      /etc/nginx/sites-available/my_env
      server {
      listen 443 ssl default_server;  #SSL Port deault
      server_name gurramlearninglabs.com;

      ssl_certificate /etc/letsencrypt/live/gurramlearninglabs.com/fullchain.pem;
      ssl_certificate_key /etc/letsencrypt/live/gurramlearninglabs.com/privkey.pe$
      location = /favicon.ico { access_log off; log_not_found off; }
      location /static/ {
      root /home/ubuntu/CloudComputingAssignments;
      }
      location /.well-known/acme-challenge {
      root /home/ubuntu/CloudComputingAssignments/letsencrypt;
      }
      location / {
      include uwsgi_params;
      uwsgi_pass unix:/run/uwsgi/my_env.sock;
      }
      
Step6:sym-link to sites-enable

      ln -s /etc/nginx/sites-available/my_env /etc/nginx/sites-enabled/my_env
      systemctl restart nginx

Adding SSL certificate

Step1:First, we need to download and install “Lets Encrypt Client”

      sudo apt-get update
      sudo apt-get install -y git 
      sudo git clone https://github.com/certbot/certbot /opt/letsencrypt

Step2:Create directory to store lets encrypty temporary files for verification

      Cd /etc/
      mkdir letsencrypt
      sudo chgrp www-data letsencrypt
        
Step3:Create file as shown below

      /etc/letsencrypt/configs/gurramlearninglabs.com.conf
      The content should be like below
        
      #the current closed beta (as of 2015-Nov-07) is using this server
      server = https://acme-v01.api.letsencrypt.org/directory

      # this address will receive renewal reminders
      email =adityagurram18@gmail.com
        
      # turn off the ncurses UI, we want this to be run as a cronjob
      text = True

      # authenticate by placing a file in the webroot (under .well-known/acme-challen$
      # and then letting LE fetch it
      authenticator = webroot
      webroot-path = /home/ubuntu/CloudComputingAssignments/letsencrypt/

Step4:Add this location to nginx server file to get access

      nano /etc/nginx/sites-available/my_env

      location /.well-known/acme-challenge {
      root /home/ubuntu/CloudComputingAssignments/letsencrypt;
      }

Step5:Verify the configuration file is syntactically valid and restart NGINX

      sudo nginx -t && sudo nginx -s reload

Step6:Requesting the certificate

      cd /opt/letsencrypt
      ./certbot-auto --config /etc/letsencrypt/configs/gurramlearninglabs.com.conf certonly
      We should get “congratulations message”
      
Step7:Pointing nginx server to certiticate in my_env file

      server {
      #add below lines to my_env file
      listen 443 ssl default_server;  #SSL Port deault
      server_name gurramlearninglabs.com;

      ssl_certificate /etc/letsencrypt/live/gurramlearninglabs.com/fullchain.pem;
      ssl_certificate_key /etc/letsencrypt/live/gurramlearninglabs.com/privkey.pe$
      }

Step8:Verify the configuration file is syntactically valid and restart NGINX

      sudo nginx -t && sudo nginx -s reload

Step9:Add redirection from http to https using below code in my_env file

      server {
      listen 80;
      server_name gurramlearninglabs.com;
      return 301 https://$host$request_uri;
      }
      
Step10:Reload the nginx server

       sudo nginx -t && sudo nginx -s reload


References:

1.	https://pythonprogramming.net/django-web-development-with-python-intro/
2.	https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04
3.	https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-14-04
4.	https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04
5.	https://www.nginx.com/blog/free-certificates-lets-encrypt-and-nginx/
6.	https://www.digitalocean.com/community/questions/run-django-python-2-and-python-3-apps-with-uwsgi-and-nginx-on-same-server
7.	http://logch.blogspot.hk/2017/02/django-uwsgi-nginx-setup-in-ubuntu-16.html
8.	https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04




