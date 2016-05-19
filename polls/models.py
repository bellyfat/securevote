from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from uuid import uuid4 as short_uuid


class Poll(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=short_uuid,
            editable=False)
    question = models.TextField()
    creator = models.OneToOneField(
            User,
            verbose_name=_('creator'))
    private = models.BooleanField(default=False)
    start_time = models.DateTimeField(
            default=timezone.now() + timezone.timedelta(hours=1))
    end_time = models.DateTimeField(
            default=timezone.now() + timezone.timedelta(days=1))
    created_time = models.DateTimeField(
            auto_now_add=True)
    modified_time = models.DateTimeField(
            auto_now=True)

    def __str__(self):
        return '{question} - [{creator}]'.format(
                question=self.question[:16],
                creator=self.creator)

    class Meta:
        db_table = 'polls'
        ordering = ['-created_time']


class Choice(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=short_uuid,
            editable=False)
    poll = models.ForeignKey(
            'Poll',
            on_delete=models.CASCADE)
    choice_text = models.CharField(
            _('text'),
            max_length=200)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        db_table = 'choices'
        ordering = ['votes']
