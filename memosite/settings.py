from pathlib import Path
import os
import django_heroku
import dj_database_url

DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# SECURITY WARNING: don't run with debug turned on in production!

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'micromemo/static'),
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

if not DEBUG:
    # Heroku settings

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Static files (CSS, JavaScript, Images)
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'
    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'micromemo/static'),
    )

    MIDDLEWARE += [
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

    SECRET_KEY = os.environ['SECRET_KEY']

    # HerokuのConfigを読み込み
    django_heroku.settings(locals())

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'micromemo',
    'accounts',
    'django.contrib.sites', # 追加
    'allauth', # 追加
    'allauth.account', # 追加
    'allauth.socialaccount', # 追加
]

ROOT_URLCONF = 'memosite.urls'

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

WSGI_APPLICATION = 'memosite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME':os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{"min_length":6},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ja-jp'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
]

AUTH_USER_MODEL = 'accounts.CustomUser'

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', #デフォルトの認証基盤
    'allauth.account.auth_backends.AuthenticationBackend',
)
 
ACCOUNT_AUTHENTICATION_METHOD = 'username' # メールアドレス（とパスワードで）認証する
ACCOUNT_USERNAME_REQUIRED = True # サインアップ（ユーザー登録）の時にユーザーネームを尋ねる
ACCOUNT_EMAIL_REQUIRED = False # サインアップ（ユーザー登録）の時にメールアドレスを尋ねる
ACCOUNT_EMAIL_VERIFICATION  = "none" # メールアドレス検証を必須化

LOGIN_URL = 'accounts:login' # ログインURLの設定
LOGOUT_URL = 'accounts:logout_complete'
LOGIN_REDIRECT_URL = '/index/frontpage' # ログイン後のリダイレクト先
ACCOUNT_LOGOUT_REDIRECT_URL = '/index/' #　ログアウト後のリダイレクト先

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'urlmemo2022@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
if not DEBUG:
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

if not DEBUG:
    db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES = {
        'default': dj_database_url.config()
    }
    ALLOWED_HOSTS = ['*']
    DATABASES['default'].update(db_from_env)