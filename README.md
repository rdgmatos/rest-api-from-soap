### Rest Api From SOAP
#### Translate rest to soap

##### Requirements

`
python 2.7
`

### How to install Python 

* https://www.python.org/downloads/

### How to install virtualenv:

###### Install **pip** first

    sudo apt-get install python3-pip

###### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

###### Now create a virtual environment 

    virtualenv venv 

>you can use any name insted of **venv**

###### You can also use a Python interpreter of your choice

    virtualenv -p /usr/bin/python2.7 venv
  
###### Active your virtual environment:    
    
    source venv/bin/activate
    
###### Using fish shell:    
    
    source venv/bin/activate.fish

###### To deactivate:

    deactivate

###### Create virtualenv using Python3
    virtualenv -p python myenv

###### Instead of using virtualenv you can use this command in Python3
    python2 -m venv myenv

### How to install dependency's 

````bash
pip install -r requirements.txt
````

##### Dependency's
```
    aniso8601==3.0.2
    appdirs==1.4.3
    attrs==18.1.0
    cached-property==1.4.3
    certifi==2018.4.16
    chardet==3.0.4
    click==6.7
    defusedxml==0.5.0
    Flask==1.0.2
    Flask-Caching==1.4.0
    Flask-RESTful==0.3.6
    gunicorn==19.9.0
    idna==2.7
    isodate==0.6.0
    itsdangerous==0.24
    Jinja2==2.10
    lxml==4.2.4
    MarkupSafe==1.0
    pytz==2018.5
    requests==2.19.1
    requests-toolbelt==0.8.0
    six==1.11.0
    urllib3==1.23
    Werkzeug==0.14.1
    zeep==3.1.0
```

### How to run app

`gunicorn run:app`

`OR`

`python app.py`


