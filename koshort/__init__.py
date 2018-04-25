import pkg_resources

__title__ = 'koshort'
__author__ = 'nyanye'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2018 Nyanye'

try:
    __version__ = pkg_resources.get_distribution('koshort').version
except pkg_resources.DistributionNotFound:
    __version__ = "dev"

from koshort.data import clear