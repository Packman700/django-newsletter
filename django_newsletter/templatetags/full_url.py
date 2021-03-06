from django import template
from django.conf import settings
from django.urls import reverse

register = template.Library()


@register.simple_tag(name="full_url")
def get_full_url(input_url, *args):
    url_domain = settings.HOST_DOMAIN
    url_directory = reverse(input_url, args=args)
    url_protocol = "http://" if settings.DEBUG else "https://"

    return url_protocol + url_domain + url_directory
