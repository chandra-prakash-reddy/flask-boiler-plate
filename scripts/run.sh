#setting the configuration environment
export CONFIG_FILE=application-$1.properties
cat $CONFIG_FILE

#running the application
gunicorn -b 0.0.0.0:$2 -w 1 --preload wsgi:app