from django import template

import json

register = template.Library()


@register.filter(name='jsonify', is_safe=True)
def jsonify(object):
    return json.dumps(object)
