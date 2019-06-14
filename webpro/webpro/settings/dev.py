from webpro.settings.base import *

print("Dev Settings active")

# Sendet Mails in Console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'