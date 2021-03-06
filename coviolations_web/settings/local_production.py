from .base import INSTALLED_APPS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['coviolations.io']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}

VIOLATIONS = (
    'violations.pep8',
    'violations.sloccount',
    'violations.py_unittest',
    'violations.pip_review',
    'violations.testem',
    'violations.coverage',
    'violations.jslint',
    'violations.xunit',
)

SERVICES = (
    'services.travis_ci',
    'services.token',
    'services.coviolations',
)

PUSH_BIND = 'https://coviolations.io/sub'
REDIS_PUSH = 'coviolations_push'

INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'ERROR',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'INFO',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'level': 'ERROR',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        "rq.worker": {
            "handlers": ["sentry"],
            "level": "ERROR",
            'propagate': False,
        },
        'coviolations_tasks': {
            'level': 'DEBUG',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'coviolations_services': {
            'level': 'DEBUG',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'coviolations_projects': {
            'level': 'WARNING',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'nodes': {
            'handlers': ['console', 'sentry'],
            'level': 'WARNING',
        },
    },
}

USE_SSL = True
