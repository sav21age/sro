from django.db import models

class IsVisibleManager(models.Manager):
    def get_queryset(self):
        return super(IsVisibleManager, self).get_queryset()\
            .filter(is_visible=True)
