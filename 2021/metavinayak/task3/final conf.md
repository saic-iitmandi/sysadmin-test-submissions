https://phoenixnap.com/kb/how-to-set-up-apache-virtual-hosts-ubuntu
https://devanswers.co/installing-apache-ubuntu-18-04-server-virtual-hosts/


sudo mkdir -p /var/www/phxnap1.com/public_html
sudo mkdir -p /var/www/phxnap2.com/public_html

(*)
sudo chown -R $USER:$USER /var/www
then
sudo chmod -R 755 /var/www



sudo nano /var/www/phxnap1.com/public_html/index.html

<html>
<head>
<title>Welcome to phoenixNAP 1!</title>
</head>
<body>
<h1>Well done! Everything seems to be working on your first domain!</h1>
</body>
</html>


sudo nano /var/www/phxnap2.com/public_html/index.html

...

sudo nano /etc/apache2/sites-available/phxnap2.com.conf

<VirtualHost *:80>
ServerAdmin webmaster@phxnap2.com
ServerName phxnap2.com
ServerAlias www.phxnap2.com
DocumentRoot /var/www/phxnap2.com/public_html

ErrorLog ${APACHE_LOG_DIR}/phxnap2.com-error.log
CustomLog ${APACHE_LOG_DIR}/phxnap2.com-access.log combined
</VirtualHost>

sudo a2ensite phxnap1.com
sudo a2ensite phxnap2.com
sudo a2ensite 000-default.com

sudo apachectl configtest

(Syntax OK message must be at end)


cd /etc/hosts

add
'127.0.0.1      phxnap1.com'
'127.0.0.1      phxnap2.com'


finally
sudo systemctl restart apache2


# Docker:

https://codeburst.io/http-server-on-docker-with-https-7b5468f72874