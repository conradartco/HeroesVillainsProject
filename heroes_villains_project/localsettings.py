

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w0!z5m#@^&3+p^i88&ey6)s^y%42^n_v&xjn^+9t&mmms8n38%'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'heroes_villains_database',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'DaisyMegan1!',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
