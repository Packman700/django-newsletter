from django.conf import settings
from django.core.mail import send_mail
from django.db import models

from .member import Member
from ..mail_factory import default_mail
from ..schedule import schedule_mail_message


class EmailMessage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    send_time = models.DateTimeField()
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.title}"

    def save(self, *args, **kwargs):
        # Insert and update
        super().save(*args, **kwargs)
        if EmailMessage.objects.filter(id=self.id):
            schedule_mail_message(self.pk, 'UPDATE', self.send_time)
        else:
            schedule_mail_message(self.pk, 'INSERT', self.send_time)

    def delete(self, *args, **kwargs):
        schedule_mail_message(self.pk, 'DELETE', self.send_time)
        super().delete(*args, **kwargs)

    @classmethod
    def send_mail_to_all_members(cls, id_):
        """Sending mail to all members"""
        members_objects = Member.objects.filter(confirmed=True)

        mail = cls.objects.filter(id=id_)
        mail.update(is_send=True)
        mail = mail.first()

        sender_email = settings.EMAIL_HOST_USER
        members_mails = [member.email for member in members_objects]
        email_content = default_mail(mail.content)

        send_mail(mail.title, "", sender_email, members_mails, html_message=email_content)
