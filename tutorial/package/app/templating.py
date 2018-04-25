from jinja2 import Environment, FileSystemLoader, StrictUndefined
from app import configuration as C


def render_file(template, **kwargs):

    env = Environment(
        loader=FileSystemLoader(C.TEMPLATE_DIR),
        undefined=StrictUndefined,
        trim_blocks=True
    )

    template = env.get_template(template)
    return template.render(**kwargs)
