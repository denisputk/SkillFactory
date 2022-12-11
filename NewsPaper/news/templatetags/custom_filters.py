from django import template


register = template.Library()

curse_words = {'Facebook', 'Twitter', 'Meta', 'Cameron'}


@register.filter()
def censor(value: str):
    for word in curse_words:
        value = value.replace(word, f'{word[:1]}******')
    return value
