# NITK RACING WEBSITE

## Abstract

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design, that follows the model-template-view (MVT) architectural pattern.The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings files and data models. Django also provides an optional administrative create, read, update and delete (CRUD) interface that is generated dynamically through introspection and configured via admin models.

Django provides a bridge between the data model and the database engine, and supports a large set of database systems including MySQL, Oracle, Postgres, etc. Django also supports NoSQL database through Django-nonrel fork. For now, the only NoSQL databases supported are MongoDB and google app engine.It consists of an object-relational mapper (ORM) that mediates between data models (defined as Python classes) and a relational database ("Model"), a system for processing HTTP requests with a web templating system ("View"), and a regular-expression-based URL dispatcher ("Controller"). 

Django REST framework is a powerful and flexible toolkit for building Web APIs.Django's configuration system allows third party code to be plugged into a regular project, provided that it follows the reusable app conventions. Django has built-in support for Ajax, RSS, Caching and various other frameworks.Django comes with a lightweight web server to facilitate end-to-end application development and testing.

The Model-View-Template (MVT) is slightly different from MVC. In fact the main difference between the two patterns is that Django itself takes care of the Controller part (Software Code that controls the interactions between the Model and View), leaving us with the template. The template is a HTML file mixed with Django Template Language (DTL)

## Models In the Website

- Members
- Images
- Sponsor
- Banner
- Pitstop
- Blog
- Document
- Subscribers

## Functionalities Implemented

- The content in terms of team members' data, images, 3D models, banners, sponsor logos, subscribers, and blog content can be uploaded via the admin dashboard by the superadmin or the user with admin permissions.

- ModelViewer has been used in order to display the 3D models that are uploaded as .glb files.

- There are appropriate filters in place for the content that is to be displayed on subsystem pages. 

- A subscription service has been implemented for the users to get updates about the latest editions of our monthly newsletter 'PITSTOP'.

- Google Maps API has been used to embed a google map the diplays the location of National Institute Of Technology, Karnataka.

- Embedding youtube video links to display the videos uploaded on the NITKRacing youtube channel.

- Dislaying Images corresponding to the model in various sections on the website pages.

## User Guidelines

1. Clone the repository.
2. Run the following commands in you terminal:

``` 
$ source venv/bin/activate
$ python3 runserver
```
3. Now enter ```localhost:8000``` in the browser.
4. To access admin dashboard, ```localhost:8000/admin``` in the browser.
