# templatetags/custom_filters.py （新規作成）
from django import template
from urllib.parse import urlencode

register = template.Library()

@register.filter
def dict2dict(dictionary, exclude_key):
    """指定したキーを除外したGETパラメータを返す"""
    new_dict = dictionary.copy()
    if exclude_key in new_dict:
        del new_dict[exclude_key]
    return urlencode(new_dict)