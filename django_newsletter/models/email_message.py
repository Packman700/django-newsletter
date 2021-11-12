from django.conf import settings
from django.core.mail import send_mail
from django.db import models

from django_newsletter.mail_factory import default_mail
from django_newsletter.models.member import Member

from datetime import datetime, timedelta


class EmailMessageAbstract(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.id} {self.title}"

    @classmethod
    def send_mail_to_all_members(cls, id_, members=None):
        """Sending mail to all members"""
        if members is None:
            members = Member.objects.filter(confirmed=True)
        # TODO ADD LOGIC TO TAKE ALSO NOT CONFIRMED USERS

        mail = cls.objects.filter(id=id_).first()

        sender_email = settings.EMAIL_HOST_USER
        members_mails = [member.email for member in members]
        email_content = default_mail(mail.content)

        send_mail(mail.title, "", sender_email, members_mails, html_message=email_content)


### DATE EMAIL ###
class EmailMessageToDate(EmailMessageAbstract):
    send_time = models.DateTimeField()
    is_send = models.BooleanField(default=False)

    @classmethod
    def send_mail_to_all_members(cls, id_, members=None):
        """Sending mail to all members"""
        super().send_mail_to_all_members(id_)

        mail = cls.objects.filter(id=id_)
        mail.update(is_send=True)


### CRON EMAIL ###
class EmailMessageCron(EmailMessageAbstract):
    # TODO Add cron validator
    cron = models.CharField(max_length=30)


### MEMBERSHIP TIME EMAIL ###
class EmailMessageMembershipTime(EmailMessageAbstract):
    """Send mail according to time left from join"""

    days_from_join = models.IntegerField(blank=True, default=0,
                                         help_text="Number of days spend from join to send this message")

    @classmethod
    def send_mail_to_all_members(cls, id_, members=None):
        """Sending mail to members"""
        mail = cls.objects.get(id=id_)
        time_to_add = timedelta(days=mail.days_from_join)
        today = datetime.now().date()
        expected_account_create_date = today - time_to_add

        members = Member.objects.filter(join_datetime__year=expected_account_create_date.year,
                                        join_datetime__month=expected_account_create_date.month,
                                        join_datetime__day=expected_account_create_date.day)

        if members:
            super().send_mail_to_all_members(id_, members)
