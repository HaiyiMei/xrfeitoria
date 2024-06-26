from .utils_logger import logger  # isort:skip
from . import constants, operators, properties, ui  # isort:skip

bl_info = {
    'name': 'XRFeitoriaBpy',
    'author': 'OpenXRLab',
    'version': (0, 0, 0),  # XXX: Would be updated by CI/CD
    'blender': (3, 3, 0),
    'category': 'Tools',
}
__version__ = version = '0.6.3'


def register():
    operators.register()
    properties.register()
    ui.register()


def unregister():
    operators.unregister()
    properties.unregister()
    ui.unregister()
