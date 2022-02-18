# Buupass

A task from buupass

## Getting Started

- clone this repo

```
$ git clone https://github.com/cliffnyendwe/buu-pass.git
```

### Prerequisites

- Python 3 latest version
- Pip3 installer
- virtualenv command

### Installing

1. cd into the Buupass folder

```
$ cd buupass
```

2. Add a python 3 environment

```
$ virtualenv env
```

3. Enter the virtual environment

```
$ source env/bin/activate
```

4. Install dependancies from requirements.txt

```
(env)$ pip install -r requirements.txt
```

5. rename .env copy to .env then run this command

```
(env) $ source .env
```

6. Run server

```
(env) $ python manage.py runserver
```

## Deployment

to deploy to heroku simply create a project and attach your git hub repository

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used


## Authors

- **Cliff**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
