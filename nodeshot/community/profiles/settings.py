from django.conf import settings


REGISTRATION_OPEN = getattr(settings, 'NODESHOT_PROFILES_REGISTRATION_OPEN', True)
EMAIL_CONFIRMATION = getattr(settings, 'NODESHOT_PROFILES_EMAIL_CONFIRMATION', True)
REQUIRED_FIELDS = getattr(settings, 'NODESHOT_PROFILES_REQUIRED_FIELDS', ['email'])
