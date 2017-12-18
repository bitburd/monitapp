# monitapp
monitapp is a django app for listing host status on one page
To use it, setup monit on one or more servers and run it as follows:
Change settings.py (ALLOWED_HOSTS) to your monitapp server ip.
Change references to /home/* to your home directory (monitapp project home directory)
Add your list of servers to (MONITAPP_HOSTS) variable in settings.py
install all scripts and code into a base project called djangoapp
copy or git clone the monitapp directory here and add it to djangoapp project
Add a admin user and a normal django user if you desire. Change their passwords.
Setup and migrate the very first djangoapp db (using sqlite3 and manage.py commands)
run the server and open port 8088 and go to http://serveripaddress:8088/monitapp/login
The status page is open to anyone: http://serveripaddress:8088/monitapp/status/
