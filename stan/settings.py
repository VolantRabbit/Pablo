from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--qja*-!$d@-^fxzb93&f38=_cr5)q$i9hlq=2jv_!z_$ets5&@'

DEBUG = True

ALLOWED_HOSTS = []
    
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stan_calc',
]

MIDDLEWARE = [
    # adds security tags prevents iframing against clickjacking
    'django.middleware.security.SecurityMiddleware',            # enhances security by adding headers Strict-Transport-Security,
                                                                # X-Content-Type-Options - prevent sniff, X-XSS-Protection,
                                                                # redirect HTTP to HTTPS if configured

    # manages session data
    'django.contrib.sessions.middleware.SessionMiddleware',     # manages session data for request, Enables the use of Django's session framework,
                                                                # which allows data to be stored across requests (e.g., user login status).
                                                                # uses cookies or other storage backends to save session data.

    # enhance request processing URL formatting
    'django.middleware.common.CommonMiddleware',                # adds various utilities for request processing
                                                                # adding a trailing slash to URLs if APPEND_SLASH is enabled
                                                                # handling URL rewriting based on settings like PREPEND_WWW
                                                                # helps enforce consistent URL formatting

    # cross-site redirect protection
    'django.middleware.csrf.CsrfViewMiddleware',                # Cross-Site Request Forgery (CSRF) protection
                                                                # adds a CSRF token to forms and checks for its presence on POST requests
                                                                # prevents malicious websites from making unauthorized requests on behalf of authenticated users

    'django.contrib.auth.middleware.AuthenticationMiddleware',  # associates user information with requests
                                                                # ensures the request.user object is available in views, templates, and other parts of the application.
                                                                # handles user authentication and login status

    'django.contrib.messages.middleware.MessageMiddleware',     # adds support for one-time notifications
                                                                # enables the use of the Django messages framework, which allows messages like "Your profile has been updated" to be displayed to users.

    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # protects against clickjacking attacks
                                                                # adds the X-Frame-Options header to HTTP responses to control whether the website can be embedded in an <iframe> tag
                                                                # prevents malicious sites from embedding your site and tricking users into performing unintended actions.
]

ROOT_URLCONF = 'stan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'stan.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
