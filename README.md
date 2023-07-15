# cs50 blog
#### Description:
This web app is created for CS50 Introduction to Computer Science course final project. 
It lets you share your stories about various subjects with other users. 
For this project I had to learn django, a bit of object oriented programming and advance my skills in html, css. 
For learning django I used CS50 web programming course, tutorials, documentations and stackoverflow.

This project has 4 different folders: blog, media, project, user

Blog folder is where web app functionality is. 
Most of the classes and functions are defined in blog/views.py, 
in blog/templates/blog folder there is main layout.html file, then there is home.html file which is made for homepage view and 
then there are post related files: post_confirm_delete.html, post_detail.html, post_form.html. post_confirm_delete.html makes sure that you want to delete post, post-detail.html gets post view page and post-form.html page makes you submit your post. 

Users folder is where user functionality is. 
I made it as a separate folder so that it is easy to distinguish and also can be easily used later in other projects. 

sqlite3 database is for storing user data and posts.

I used pillow as a resizing tool for profile pictures and crispy-forms as a design improvement.

Below are given requirements used to run and instructions on how to run code locally.


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

Create database

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

Start the server

```bash
  python3 manage.py server
```
