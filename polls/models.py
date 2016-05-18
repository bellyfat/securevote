from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    question = models.TextField()
    creator = models.OneToOneField(
            User,
            verbose_name=_("Creator"))
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    created_time = models.DateTimeField(
            auto_now_add=True)
    modified_time = models.DateTimeField(
            auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'polls'
        ordering = ['-created_time']
