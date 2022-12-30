## Introduce

DEMO: https://port-0-python-django-work-system-53px25lbxplfd0.gksl2.cloudtype.app/

Developing : 22/12/21 ~ ( 23/1/8 )

Work(your project)
Commission(request for other team or task you have to)
I am building a system that could be replaced with current paper system in ordinarily old my company. The papaer system has demerit that you cant grasp the current work situation, which one has been done or not.. , we need visible and flexible one.

I have been trying **simple, light, ease-to-use** work manage system.
In this system, you can create a work(project) and make commissions which should be completed **by other department**. you can manage your team member's or your works **visibly and flexibly**.

### version
```
Django 3.1.13
python 3.9
```

```
git clone https://github.com/zzaizzai/python-django-work-system.git
cd python-django-work-system
pip install -r requirements.txt
python manage.py runserver
```

admin 1234
other users password: qwer1234qwer


### env
```
DJANGO_SECRET=
MYSQL_USER_PW=
MYSQL_HOST=
MYSQL_PORT=
```

### RECORD
```
22/12/21 created this project
12/24 created basic frame (works and commissions)
12/25 show commissions as child in work page
12/27 add comments at work and commission page
12/29 changed permission of edit, cancle buttons in work and commission (all users -> team users)
12/30 add history of work
```

I appreciate Cloud Cype (https://cloudtype.io/) for free and fast hosting service

---

# django-boilerplate

A faster way to getting started with your Django project. Have your django project up and running in no-time

## Getting started

- clone this repository using: `git clone https://github.com/beingbiplov/django-boilerplate.git`
- Move into the directory: `cd django_boilerplate`
- Create a virtual environment and activate it.
- Install dependencies with: `pip install -r requirements.txt`
- Rename your project with: `python manage.py rename <current_project_name> <new_project_name>`

Now, you are all ready to go. This django project boilerplate comes with an app called `core` where you can get started right away. `urls.py`, `templates` and `static` are all setup at app level.
You can start the server using: `python manage.py runserver` and navigate the default home page at: `localhost:8000`

## License

This project is licensed under the MIT license, Copyright (c) 2020 django-boilerplate. For more information see [LICENSE].

[license]: https://github.com/beingbiplov/django-boilerplate/blob/master/LICENSE
