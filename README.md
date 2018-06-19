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


## Set Up


Download the project zip file to you computer and unzip the file. Or clone this repository to your desktop.

### OAuth setup
In order to log in to the web app, you will need to get either a Google+ or Facebook OAuth app ID and secret key. 

For Google, go to the
[Google Developers Console](https://console.developers.google.com/) and for Facebook,
go to [Facebook Login](https://developers.facebook.com/products/login).

Once you have your credentials, put the IDs and secrets in the `fb_client_secrets.json`
file for Facebook and `g_client_secrets.json` for Google.


### Usage

Bringing the VM up

Launch the Vagrant VM from inside the vagrant folder with the following command:


```bash
vagrant up
```
log into the VM with the following command:

```bash
vagrant ssh
```

move inside the catalog folder:

```bash
cd /vagrant/catalog
```
Then run the application:

```bash
python application.py
```

Now you are able to browse the application at this URL:

```bash
http://localhost:8000/
```
 Screenshots
-----


<img src="https://github.com/IrinaSerova/JustLearn/blob/master/catalog/static/images/Screen1.png">

<img src="https://github.com/IrinaSerova/JustLearn/blob/master/catalog/static/images/Screen2.png">
-----
<img src="https://github.com/IrinaSerova/JustLearn/blob/master/catalog/static/images/Screen3.png">
-----

<p align="center">
  <img src="https://github.com/IrinaSerova/JustLearn/blob/master/catalog/static/images/Screen4.png" width="80%">
</p>