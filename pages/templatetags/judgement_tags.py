from django import template

register = template.Library()


@register.filter(name="relevant_text")
def get_relevant_text(judgement, query):
    return judgement.get_relevant_text_main_func(query)
