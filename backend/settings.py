"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$2s81)%!49cba64kgl0hbrwk3y0yqfch$a408h##)6u_$6mrij'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.percale.com.ua']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # pip install django-ckeditor
    'ckeditor',
    'ckeditor_uploader',
    # pip install django-mptt
    'mptt',
    # pip install transliterate
    'transliterate',
    # pip install djangorestframework
    'rest_framework',
    'rest_framework.authtoken',
    #pip install django-filter
    'django_filters',
    # pip install django-cors-headers
    'corsheaders',
    'product',
    # 'orders',
    'users',
    # pip install djoser
    'djoser',
    'order',
    'userCabinet',
    'home',
    'blog',
    'wishlist',
    'quethen',
    'index',
    'detskoePostelnoe',
    'odeyala',
    'pled',
    'podushki',
    'pokryvala',
    'polotenca',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # добавим corsheaders
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'backend.urls'

# добавим corsheaders
CORS_ORIGIN_ALLOW_ALL = True
# CORS_URLS_REGEX = r'^/api/.*$'
CORS_ORIGIN_WHITELIST = (
'http://localhost:4200',
)

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static"),
)
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")



# Настройки ckeitor

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default':{
        'toolbar': 'None',
 'height': 200,
 'width': 800,
 'extraPlugins':'codesnippet',
    },
}

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':(
        # 'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 'PAGE_SIZE':10,

    'DEFAULT_AUTHENTICATION_CLASSES':(
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)

    # 'EXCEPTION_HANDLER':
    #     'rest_framework_json_api.exceptions.exception_handler',
    # # 'DEFAULT_PAGINATION_CLASS':
    # #     'rest_framework_json_api.pagination.PageNumberPagination',
    # 'DEFAULT_PARSER_CLASSES':(
    #     # 'rest_framework_json_api.parsers.JSONParser',
    #     'rest_framework.parsers.FormParser',
    #     'rest_framework.parsers.MultiPartParser',
    # ),
    # 'DEFAULT_RENDERER_CLASSES':(
    #     # 'rest_framework_json_api.renderers.JSONRenderer',
    #     'rest_framework.renderers.BrowsableAPIRenderer',
    #    ),
    # 'DEFAULT_METADATA_CLASS':'rest_framework_json_api.metadata.JSONAPIMetadata'
}

# AUTH_USER_MODEL = 'authapp.User'
DJOSER = {
    'LOGIN_FIELD': 'email',}
#     'USER_CREATE_PASWORD_RETYPE':True,
#     'SERIALIZERS':{
#         'user_create':'authapp.serializers.UserCreateSerializer',
#         'user':'authapp.serializers.UserCreateSerializer',
#         # 'current_user':'authentication.serializers.CurrentUserSerializer',
#     }
# }
