# cs50 blog
#### Video Demo:  <URL HERE>
#### Description:
This web app is created for CS50 Introduction to Computer Science course final project. It lets you share your stories about various subjects with other users. For this project I had to learn django, a bit OOP and advance my skills in html, css. For learning django I used CS50 web programming course, tutorials, documentations and stackoverflow.

This project has 4 different folders: blog, media, project, user

Blog folder is where web app functionality is. Most of the classes and functions are defined in blog/views.py, in blog/templates folder there is main layout.html file, homepage file and post related files.

Media folder is where profile pictures are stored.

Project folder is nearly unchanged after django configuration, just added some paths in urls.py file and added some lines in settings.py

Users folder is where user functionality is. I made it as a separate folder so that it is easy to distinguish and also can be easily used later in other projects.

sqlite3 database is for storing user data and posts.

I used pillow as a resizing tool for profile pictures and crispy-forms for design improve.



#### Requirements to run
* Django
* django-crispy-forms
* Pillow

#### Run Locally

Clone the project

```bash
  git clone https://github.com/mdiko/projectcs50.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python3 manage.py server
```
