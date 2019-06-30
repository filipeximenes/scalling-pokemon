from IPython.core.display import display as idisplay, HTML
import pprint
from django.template.loader import get_template
from django.db import connection
import timeit as pytimeit


def pretty(*args, **kwargs):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(*args, **kwargs)


def display(html):
    idisplay(HTML(html))


def show_template(template_name):
    template = get_template(template_name)
    pretty(template.template.source)


def render(template_name, context, show=False):
    template = get_template(template_name)

    html = template.render(context=context)

    if show:
        display(html)


def timeit(func):
    total = pytimeit.timeit(func, number=1)
    print('Ran in:', total)


class count_queries:
    def __init__(self):
        self.queries = []

    def __enter__(self):
        self.initial = len(connection.queries)
        return self

    def __exit__(self, *args, **kwargs):
        self.queries = [q['sql'] for q in connection.queries[self.initial:]]
        print('Number of queries:', len(self.queries))
