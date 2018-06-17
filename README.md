# JustLearn

Just Learn Item Catalog project is a part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).


## Description
Just Learn Item Catalog App stores a list of  of  Courses within a variety of categories for Learning Full Stack Web Development.  Authenticated users have the ability to post, edit, and delete their own items.


## Requirements
The project code requires the following software:

* Python
* [SQLAlchemy](http://www.sqlalchemy.org/) 
* [Flask](http://flask.pocoo.org/) 
* The following Python packages:
    * oauth2client
    * requests
    * httplib2
    * flask-seasurf (a CSRF defence)


## Usage

Download the project zip file to you computer and unzip the file. Or clone this repository to your desktop.


### Bringing the VM up

Launch the Vagrant VM from inside the vagrant folder with the following command:


```vagrant up
```
log into the VM with the following command:

```vagrant ssh
```

move inside the catalog folder:

```cd /vagrant/catalog
```
Then run the application:

```python application.py
```

Now you are able to browse the application at this URL:

```http://localhost:8000/
```