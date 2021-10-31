from django import forms
from django.conf import settings

from django_newsletter.exceptions import WhiteListValidationError, BlackListValidationError
from django_newsletter.models.access_lists import WhiteList, BlackList
from django_newsletter.models.member import Member


class JoinNewsletterForm(forms.ModelForm):
    NEED_CONFIRM = settings.NEED_CONFIRM_JOIN_TO_NEWSLETTER

    confirmed = forms.BooleanField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Member
        fields = [
            'email',
            'username',
            'confirmed'
        ]

    def clean_confirmed(self):
        self.confirmed = not self.NEED_CONFIRM
        return self.confirmed

    def clean_email(self):
        email = self.cleaned_data['email']
        if settings.ENABLE_WHITE_LIST and not WhiteList.contains(email):
            valid_domains = WhiteList.objects.first().email_domain
            raise WhiteListValidationError(
                "Your email isn't in whitelist you can try %(valid_domain)s",
                params={'valid_domain': valid_domains},
                code='white list error'
            )

        if settings.ENABLE_BACK_LIST and BlackList.contains(email):
            raise BlackListValidationError(
                "Your email is in blacklist try something else",
                code='black list error'
            )

        return email
