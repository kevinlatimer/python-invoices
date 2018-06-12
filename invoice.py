import jinja2 as jj
import subprocess
from pathlib import Path
from tempfile import mkdtemp

class Invoice():
    def __init__(self, template_file=None, template=None):
        template_method = [i is not None for i in [template_file, template]]
        if all(template_method):
            raise RuntimeError("both a template and a template file are specified.")
        elif not any(template_method):
            raise RuntimeError("neither template nor template file were specified.")

        self.environment = jj.Environment(
            block_start_string='\\block{',
            block_end_string='}',
            variable_start_string='\\var{',
            variable_end_string='}',
            comment_start_string='%',
            comment_end_string='\n',
            trim_blocks=True,
            autoescape=False,
            enable_async=True,
        )

        if template_file:
            self.template_file = template_file
            with open(template, 'r') as f:
                self.template = jj.Template(f.readlines())

        if template:
            self.template = jj.Template(template)

    def add_item(self, name, price, quantity=1):

    def render(self, output_file, overwrite=False, passes=3, using="pdflatex", with_options="--interaction=nonstopmode"):
        output_path = Path(output_file)

        if output_path.exists() and not overwrite:
            raise RuntimeError("output file already exists. To force overwrite, invoke with 'overwrite=True'")

        process = [using] + with_options.split(" ") + latex_temporary_file
        subprocess.run(process)