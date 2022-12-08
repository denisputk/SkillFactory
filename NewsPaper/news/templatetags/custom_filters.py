from django import template


register = template.Library()

curse_words = {'Facebook', 'Twitter', 'Meta', 'Cameron'}

@register.filter()
def censor(value: str):
    try:
        if not isinstance(value, str):
            raise CensorException('Error')
        for word in curse_words:
            value = value.replace(word, f'{word[:1]}******')
        return value
    except CensorException as e:
        print(e)
