import webbrowser
import os
from jinja2 import Environment, FileSystemLoader


def render_template(rows, columns):
    env = Environment(loader=FileSystemLoader((os.path.dirname(__file__))))
    template = env.get_template('index.html')
    op = template.render(columns=columns, rows=rows)
    with open("temp.html", "w") as fh:
        fh.write(op)
    webbrowser.open_new_tab("temp.html")
