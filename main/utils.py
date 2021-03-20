

import random


def convert_name_to_slug(name):
    """
    Returns the name with appropriate formatting for using as url
    """
    slug = name.lower().replace(' ','-')
    return slug


def random_color():
    r = lambda: random.randint(0,255)
    return('#%02X%02X%02X%02X' % (r(),r(),r(),r()))
