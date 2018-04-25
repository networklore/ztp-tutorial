from jinja2 import Environment, FileSystemLoader, StrictUndefined

templates_path = '/opt/ztp/templates'


def render_file(template, **kwargs):

    env = Environment(
        loader=FileSystemLoader(templates_path),
        undefined=StrictUndefined,
        trim_blocks=True
    )

    template = env.get_template(template)
    return template.render(**kwargs)
