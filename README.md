# djsf
A single folder django template that skips a lot of boilerplate.

**Includes:**

- Single folder structure
- Django Debug Toolbar
- Django Browser Reload
- Deploy with dokku
- django-tasks
- A cusome user model
- `settings.py` file configured for Deployment and Testing
- Pytest
- Improved SQLite configuration
- Whitenoise for static files
- uv for dependency and environment management

# Project setup

This project assumes that you've already go:

- [uv](https://github.com/astral-sh/uv) installed
- A server that is running [Dokku](https://dokku.com/)
- Github
- Mac/Linux. Some things might be different for a windows computer.

## First steps

## On Github

- [ ] Create a new repository on Github from the [djsf template](https://github.com/sglmr/djsf)
- [ ] Configure dokku repository secrets on Github
    - secret: `VPS_IP`
    - secret: `SSH_PRIVATE_KEY`
    - vars: `APP_NAME`

## Clone the repository

- [ ] Clone the github project to your local computer.
- [ ] <kbd>ctrl</kbd>+<kbd>f</kbd> and replace `djsf` with the desired project name.
- [ ] rename the `djsf` folder to the desired project name
- [ ] <kbd>ctrl</kbd>+<kbd>f</kbd> and replace `djsf.domain.me` with the desired project url.

## DNS configuration

- [ ] If you want the site to be available under your domain i.e. `djsf.domain.me` then update your DNS settings to point at the server

## On the Dokku server

First, SSH into the server

```sh
ssh user@server_ip
```

Then set up a new app with the following commands:

```sh
# Create a new dokku app
dokku apps:create djsf

# Set the proxy domain for the new app
dokku domains:set djsf djsf.domain.me

# Enable letsencrypt for https
# (this will fail until the app is deployed)
dokku letsencrypt:enable djsf

# Set project environment variables
dokku config:set djsf SECRET_KEY="something-super-secret"

dokku config:set djsf ALLOWED_HOSTS="djsf.domain.me,172.12.0.2"
```

## Back to your local machine

- [ ] install [uv](https://github.com/astral-sh/uv)
- [ ] run `uv sync` to set up a virtual environment with all the dependencies.
- [ ] check for outdated dependencies with `uv pip list --outdated`
- [ ] Make sure your IDE has the correct virtual environment selected
- [ ] Run `python manage.py collectstatic --no-input`
- [ ] Test the project to make sure everything is working by running `pytest`
- [ ] Add a git remote to deploy the app `git remote add dokku dokku@server-ip:djsf`
- [ ] Push the app to dokku with `git push dokku main` (or use a different branch than main)

**Go to `https://djsf.domain.me`** and 🤞 it works!!

# Environment Variables

This project is dependent on several environment variables:

- **ALLOWED_HOSTS** - A comma separated list of allowed hosts for the Django App. typically 
- **DEBUG** - This should be `False` in production.
- **DOKKU_APP_TYPE** - If this variable exists, the project is in 'production' and will set **DEBUG** to `False` and disable django-debug-toolbar
- **SECRET_KEY** - The project will generate a random secret key if one is not set.
- **DJANGO_STATIC_HOST** - Use this if you are serving the static files from somewhere outside the app domain like `files.domain.me`

