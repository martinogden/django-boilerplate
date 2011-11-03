from path import path

from .common import STATIC_ROOT

# django-compressor
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSMinFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
