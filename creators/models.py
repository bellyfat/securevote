from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


class BaseCreatorManager(models.Manager):

    @classmethod
    def normalize_email(cls, email):
        email = email or ''

        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])

        return email

    @classmethod
    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})


class CreatorManager(BaseCreatorManager):
    use_in_migrations = True

    def create_user(self, email=None):

        if not email:
            raise ValueError(_('user must have email'))

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.save(using=self._db)
        return user


class AbstractCreator(models.Model):
    email = models.EmailField(
            _('email address'))

    objects = CreatorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('creator')
        verbose_name_plural = _('creators')
        abstract = True

    def get_username(self):
        return getattr(self, self.USERNAME_FIELD)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.get_username()


class Creator(AbstractCreator):

    class Meta:
        swappable = 'AUTH_USER_MODEL'
