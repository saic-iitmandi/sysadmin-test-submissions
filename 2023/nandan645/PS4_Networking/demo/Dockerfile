FROM httpd:2.4

# Change the listening port
RUN sed -i 's/Listen 80/Listen 8080/' /usr/local/apache2/conf/httpd.conf

COPY . /usr/local/apache2/htdocs/
