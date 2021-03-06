"""
Django settings for Bloger project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g)0^kn*5fuj@+!@v)6lafb8fc_u+4#$s+%0fc0&^$p*vcmg0))'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'tinymce'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Bloger.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Bloger.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'Blog',
        # 'HOST': 'localhost',
        # 'USER': 'root',
        # 'PASSWORD': '123456',
        # 'PORT': 3306,


    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

MEDIA_ROOT=os.path.join(BASE_DIR, r'static/uploadfiles')


# 激活邮件服务配置
# smtp服务器
EMAIL_HOST = 'smtp.163.com'
# smtp服务器的端口25/465
EMAIL_PORT = 465
EMAIL_USE_SSL=True
#·发送者的邮箱
EMAIL_HOST_USER = '15736736120@163.com'
# 授权码
EMAIL_HOST_PASSWORD = 'zxcvbnm123456'
# 收件人看到的发件人信息
EMAIL_FROM = 'Python<15736736120@163.com>'



# 富文本编辑器
TINYMCE_DEFAULT_CONFIG = {
    'theme':'advanced',
    'width':600,
    'height':400
}


# 数据库缓存配置
# CACHES = {
#     'default':{
#         'BACKEND':'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION':'my_cache_table',
#     }
# }

# 文件缓存
# CACHES = {
#  'default': {
#   'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache', #
#   'LOCATION': '/var/tmp/django_cache',        #
#   'TIMEOUT':300,              #
#   'OPTIONS':{
#    'MAX_ENTRIES': 300,            #
#    'CULL_FREQUENCY': 3,           #
#   }
#  }
# }

# redis 缓存
CACHES = {
    'default':{
        'BACKEND':'django_redis.cache.RedisCache',#
        # 'LOCATION':'redis://:123@127.0.0.1:6379/1', #
       'LOCATION':'redis://127.0.0.1:6379/1', #
    }
}



