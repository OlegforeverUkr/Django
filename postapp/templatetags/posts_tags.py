from django import template
from postapp.models import Topic

register = template.Library()

@register.simple_tag
def get_topics():
    return Topic.objects.all()