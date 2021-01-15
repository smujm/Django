"""
设置相关

Django settings for BookManager project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm9&e0*a_!3k1b8r-kr=v1_10((44-_44$3$h)f2(r@4a+h-2*$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# 安装/注册 子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login.apps.LoginConfig',   # login.apps.LoginConfig = login
    'bbs',   # '子应用名' 或 '子应用名.apps.子应用名Config'
    'book.apps.BookConfig',
    # 'pay.apps.PayConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF 使我们工程的url的配置入口
# 默认是 工程名.urls。 可以修改，但默认我们不修改
ROOT_URLCONF = 'BookManager.urls'


# 模板相关的配置信息
TEMPLATES = [
    {
        # 'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'BACKEND': 'django.template.backends.jinja2.Jinja2',    # 修改为jinja2模板
        # DIRS 设置模板路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'book.jinja2_env.environment',   # 指定jinja2的环境
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',    # 修改为jinja2模板
        # DIRS 设置模板路径
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

WSGI_APPLICATION = 'BookManager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# sqlite 主要是一个嵌入式的关系型数据库
#           主要在移动端使用
#           属于小型的关系型数据库
# 中型的数据库：mysql，sqlserver
# 大型数据库：oracle, DB2
DATABASES = {
    'default': {
        # engine 引擎
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'root',
        'NAME': 'book_manager', # 指定数据库
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# django是如何区分 静态资源和动态资源的呢？
# 就是通过 STATIC_URL
# 我么在访问静态资源 http://ip:port + STATIC_URL + 文件名
# django就会认为我么在访问静态资源，这个时候回去静态资源文件夹中进行匹配


STATIC_URL = '/static/'
# 告知系统静态文件在哪里
STATICFILES_DIRS =[
    os.path.join(BASE_DIR, 'static')
]
