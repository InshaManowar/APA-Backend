from django import template
from home.models import Video

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Video.objects.all().order_by('-created_time')[:num]