from IPython.core import display as idisplay
import pprint
from django.template.loader import get_template
from django.utils.html import escape
from django.db import connection
import timeit as pytimeit


def pretty(*args, **kwargs):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(*args, **kwargs)


def display_html(html):
    idisplay.display(idisplay.HTML(html))


def display_file(file_name):
    with open(file_name, 'r') as f:
        file = f.read()
        idisplay.display(idisplay.HTML(f'<pre>{file}</pre>'))


def display_template(template_name):
    file_name = f'pokemon/templates/{template_name}'
    with open(file_name, 'r') as f:
        file = escape(f.read())
        idisplay.display(idisplay.HTML(f'<pre>{file}</pre>'))


def render(template_name, context, show=False):
    template = get_template(template_name)

    html = template.render(context=context)

    if show:
        display_html(html)


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
