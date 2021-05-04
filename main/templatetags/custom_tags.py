from django import template
register = template.Library()

@register.simple_tag
def modify_name(book):
    if book.title_pt == 'nan':
        return book.title_en 
    else:
        return book.title_pt
    
register.filter('modify_name', modify_name)