# -*- coding: utf-8 -*-
"""
Micropolar:
http://micropolar.org/
https://github.com/biovisualize/micropolar/
"""
from IPython.html import widgets
from IPython.utils.traitlets import Unicode, Int
from jinja2 import Environment, PackageLoader

from sticky.core import Chart


ENV = Environment(loader=PackageLoader('sticky', 'templates/micropolar'))


class Micropolar(widgets.DOMWidget, Chart):

    kind = 'micropolar'
    render_template = ENV.get_template('micropolar_widget.js')

    _view_name = Unicode('Micropolar', sync=True)
    chart_id = Unicode(sync=True)
    height = Int(sync=True)
    width = Int(sync=True)

    def __init__(self, height=250, width=250, *args, **kwargs):
        """Micropolar D3 Library Widget"""
        super(Micropolar, self).__init__(*args, **kwargs)
        self.height = height
        self.width = width
        self.init_widget_js()
