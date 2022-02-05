from django.contrib import admin
from .models import appointment, feedback, payment, recent, user, worker

admin.site.register(user)
admin.site.register(worker)
admin.site.register(payment)
admin.site.register(appointment)
admin.site.register(feedback)
admin.site.register(recent)