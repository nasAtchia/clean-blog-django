# Installation

This document details the step to install the project on your local environment.

Server requirements:

- Python 3.8+
- [Pipenv](https://pypi.org/project/pipenv/) installed
- Git installed

#### Clone the project

Run the command below to clone the project from Git.

```
$ git clone https://github.com/nasAtchia/clean-blog-django.git
```

#### Create your database

Create your database on your MySQL server and import the latest ****.mysql.gz**** file from the [db](../db) folder.

#### Create your virtual environment

Create your virtual environment for the project by following the below steps:

1. Create a **.venv** directory in the project directory.
2. `pipenv --python {version}`. Replace the `{version}` with your Python version.
3. `pipenv shell`
4. `pipenv install --dev`

#### Configure your .env file

Copy the [.env.example](../cleanblog/.env.example) file and rename to .env and update the configurations according to your environment.

#### Update your media files directory

Create a `/path/to/project/media` directory. Extract and copy the latest **.tar.gz** file from the [resources'](../resources) directory.