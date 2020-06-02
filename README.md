# flask-boiler-plate   [![Build Status](https://travis-ci.org/chandra-prakash-reddy/flask-boiler-plate.svg?branch=master)](https://travis-ci.org/chandra-prakash-reddy/flask-boiler-plate)
This project provides the production ready boiler plate  to start Rest Api development in python using flask


# PreRequisites # 
   * Install Python3
      * installation  : https://www.python.org/downloads
      * documentation : https://docs.python.org/3
   * Maven
      * installation  : https://pip.pypa.io/en/stable/installing
      * documentation : https://pip.pypa.io/en/stable
   * Git 
      * installation  : https://git-scm.com/downloads
      * documentation : https://git-scm.com/doc 


# SetUp #
   * clone the repository  ***git clone <repo_url>***
   * setup flask virtual environment ***https://flask.palletsprojects.com/en/1.1.x/installation***


# Tests #
   * install dependencies :  ***pip install -r requirements.txt***
   * Run TestCases : ***pytest tests --doctest-modules --junitxml=junit/test-results.xml***
   * Code Coverage : ***py.test -v --cov=publication --cov=common --cov-report xml --cov-report html***


# Deployment #
   * Standalone
      * install dependencies  ***pip install -r requirements.txt***
      * python wsgi.py ***(recomended for development)***
      * ./scripts/run.sh <enviroment> <port>
         * enviroment ***example:-dev,prod***
         * port ***example:-2556***

  
# Verify #
   * open ***http(s): // <host\>:<port\>***  in web browser
       * example http://localhost:2556
   * documentation of apis will be available 
    
# References #
   * Flask-RestPlus ***https://flask-restplus.readthedocs.io/en/stable/swagger.html#headers***
   * SqlAlchemy Docs ***https://docs.sqlalchemy.org/en/13/orm/query.html***
