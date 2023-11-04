from django.contrib import admin

from narrator import models

admin.site.register(models.Character)
admin.site.register(models.CharacterInteraction)
admin.site.register(models.Resource)
