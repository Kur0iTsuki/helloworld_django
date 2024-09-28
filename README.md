# Hello World Django App

This is a simple Django application that returns a "Hello World" message in both JSON and HTML formats.

## Features
- A single route (`/hello/`) that returns either:
  - A JSON response: `{"Message": "Hello World!"}`
  - An HTML page with "Hello World!" in bold.

## Prerequisites

- Python 3.x
- Django (Version 3.x or above)

## How to Run the App

  ### 1. Clone the Repository
   ```sh
    git clone <https://github.com/Kur0iTsuki/helloworld_django>
    cd helloworld_django
    cd helloworld_project
   ```
2. Set Up a Virtual Environment (Optional but recommended)
```sh
  python -m venv env
  source env/bin/activate  # On Windows use: env\Scripts\activate
  ```
3.Install Django
  ```sh
pip install django
```
4.Run the Django Development Server
```sh
python manage.py runserver
```
5.Access the App
  To access the JSON response, visit:
  ```sh
http://127.0.0.1:8000/hello/?format=json
```
  output
  ```sh
{"Message": "Hello World!"}
```
To view the HTML response, visit:
```sh
http://127.0.0.1:8000/hello/
```
