from flask import Flask
from flask_babel import Babel
import urllib

from config import constants

class MyFlask(Flask):
    def get_send_file_max_age(self, name):
        if name.startswith('js/') or name.startswith('css/'):
            return 0
        return super(MyFlask, self).get_send_file_max_age(name)

app = MyFlask(__name__,
    template_folder=constants.TEMPLATE_ROOT,
    static_folder=constants.STATIC_ROOT)

app.jinja_env.filters['quote_plus'] = lambda u: urllib.quote_plus(u)