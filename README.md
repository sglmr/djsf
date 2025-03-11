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

## Setup

### Local development

This project uses [uv](https://github.com/astral-sh/uv) to manage dependencies.

```sh
# Start 
uv init

# Add dependencies
uv add django

# Update dependencies
uv sync
```

### Dokku server

```sh
```
