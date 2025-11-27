from pathlib import Path

from config.env import settings

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = settings.SECRET_KEY
DEBUG = settings.DEBUG

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'modeltranslation',  # must be before django.contrib.admin
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'order.apps.OrderConfig',
    'product.apps.ProductConfig',

    'rest_framework',
    'payme',
    'click_up'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'uz'

LANGUAGES = [
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
    ('en', 'English'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz', 'ru', 'en')

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

PAYME_ID = settings.PAYME_ID
PAYME_KEY = settings.PAYME_KEY
PAYME_ACCOUNT_FIELD = settings.PAYME_ACCOUNT_FIELD
PAYME_AMOUNT_FIELD = settings.PAYME_AMOUNT_FIELD
PAYME_ACCOUNT_MODEL = settings.PAYME_ACCOUNT_MODEL
PAYME_ONE_TIME_PAYMENT = settings.PAYME_ONE_TIME_PAYMENT
PAYME_DISABLE_ADMIN = settings.PAYME_DISABLE_ADMIN
PAYME_TEST_MODE = settings.PAYME_TEST_MODE

CLICK_SERVICE_ID = settings.CLICK_SERVICE_ID
CLICK_MERCHANT_ID = settings.CLICK_MERCHANT_ID
CLICK_SECRET_KEY = settings.CLICK_SECRET_KEY
CLICK_ACCOUNT_MODEL = settings.CLICK_ACCOUNT_MODEL
CLICK_AMOUNT_FIELD = settings.CLICK_AMOUNT_FIELD
CLICK_DISABLE_ADMIN = settings.CLICK_DISABLE_ADMIN
