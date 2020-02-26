"""calibrestekje module."""

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution('calibrestekje').version
except Exception:
    __version__ = 'unknown'
