# This is the MySQL test settings file for use with VSTS CI.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoci',
        'USER': None,
        'PASS': None,
    },
    'other': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangociother',
        'USER': None,
        'PASS': None,
    }
}

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
