"""
 Eqip

                             -------------------
        begin                : 2022-05-23
        copyright            : (C) 2022 by MapsPeople
        email                : chen@mapspeople.com
        git sha              : $Format:%H$

"""

import logging

from .constants import *


def python_version_check(major: int = 3, minor: int = 8) -> None:
    """description"""
    import sys

    assert sys.version_info.major == major and sys.version_info.minor >= minor, (
        f"This project is utilises language features only present Python {major}.{minor} and greater. "
        f"You are running {sys.version_info}."
    )


python_version_check()

__version__ = VERSION
__author__ = PLUGIN_AUTHOR


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load qlive class from file qlive.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .eqip_plugin import EqipPlugin

    if True:
        try:
            from jord.qgis_utilities.helpers import setup_logger

            setup_logger(__name__, logger_level=logging.DEBUG)
        except ImportError:
            ...

    return EqipPlugin(iface)
