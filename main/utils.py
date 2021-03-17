

def convert_name_to_slug(name):
    """
    Returns the name with appropriate formatting for using as url
    """
    slug = name.lower().replace(' ','-')
    return slug