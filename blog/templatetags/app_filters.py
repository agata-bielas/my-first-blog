from django import template
#from datetime import date, timedelta

register = template.Library()


@register.filter(name='get_polish_endings_of_the_word_comment')
def get_polish_endings_of_the_word_comment(value):
    '''
    Polska odmiana słowa komentarz:
    1 - komentarz
    0, 5, 6, ..., [10 - 21], [25 - 31], [35 - 41], itd - komentarzy
    2, 3, 4, 22, 23, 24, 32, 33, 34, itd - komentarze
    '''
    comments = value

    if comments % 10 in [2, 3, 4] and comments % 10 not in [12, 13, 14]:
        return 'komentarze'
    elif comments == 1:
        return 'komentarz'
    else:
        return 'komentarzy'
