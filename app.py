# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 18:12:13 2021

@author: Julio
"""

import pathlib
import os

from flask import Flask
from flask_babel import Babel
from flask_bootstrap import Bootstrap

from kerko import blueprint  as kerko_blueprint
from kerko.composer import Composer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ciencia123'  # Replace this value.
app.config['KERKO_ZOTERO_API_KEY'] = 'Luoum41MvIMNqSLTitax7URA'  # Replace this value.
app.config['KERKO_ZOTERO_LIBRARY_ID'] = '2635555'  # Replace this value.
app.config['KERKO_ZOTERO_LIBRARY_TYPE'] = 'group'  # Replace this value if necessary.
app.config['KERKO_DATA_DIR'] = str(pathlib.Path(__file__).parent / 'data' / 'kerko')
app.config['KERKO_FACET_COLLAPSING'] = 'True'
app.config['KERKO_COMPOSER'] = Composer()
port = os.environ.get("PORT", 5000)
babel = Babel(app)
bootstrap = Bootstrap(app)
app.run(debug=False, host="0.0.0.0", port=port)
app.register_blueprint(kerko_blueprint, url_prefix='/bibliography')
