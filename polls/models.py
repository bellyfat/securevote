from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db.models import F, Sum
from uuid import uuid4 as short_uuid


class Creator(models.Model):
    email = models.EmailField(
            primary_key=True,
            null=False,
            blank=False)
    gpg_home = models.FileField()
    created_time = models.DateTimeField(
            auto_now_add=True)
    modified_time = models.DateTimeField(
            auto_now=True)

    def __str__(self):
        return self.email

    def validate_email(self):
        pass

    class Meta:
        db_table = 'creators'


class Poll(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=short_uuid,
            editable=False)
    question = models.TextField()
    creator = models.ForeignKey(
            Creator,
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

    @property
    def finished(self):
        return self.end_time <= timezone.now()

    def vote_for(self, choice_id):
        Choice.objects.filter(
            pk=choice_id).update(votes=F('votes')+1)

    @property
    def total_votes(self):
        return self.choice_set.aggregate(
            total_votes=Sum('votes'))['total_votes']

    def get_winner_choice(self):
        return self.choice_set.filter(votes__gte=1).order_by('-votes').last()

    def __str__(self):
        return '{question} - [{creator}]'.format(
                question=self.question[:16],
                creator=self.creator)

    class Meta:
        db_table = 'polls'
        ordering = ['-created_time', 'choice__votes']


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

    @property
    def html_color_class(self):
        if self.votes <= 5:
            return "danger"
        elif self.votes <= 10:
            return "warning"
        elif self.votes <= 15:
            return "info"
        elif self.votes <= 20:
            return "success"
        else:
            return "primary"

    def get_vote_percentage(self):
        return round(float(self.votes)*100/float(self.poll.total_votes), 2)

    class Meta:
        db_table = 'choices'
        ordering = ['votes']
