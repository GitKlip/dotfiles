""" utilities related to importing files. """
import sys


class ImportStringError(ImportError):
    """Provides information about a failed :func:`import_string` attempt.

    Copied from the werkzeug library, which is BSD-3 licensed.
    """

    #: String in dotted notation that failed to be imported.
    import_name = None
    #: Wrapped exception.
    exception = None

    def __init__(self, import_name, exception):
        self.import_name = import_name
        self.exception = exception

        msg = (
            "import_string() failed for %r. Possible reasons are:\n\n"
            "- missing __init__.py in a package;\n"
            "- package or module path not included in sys.path;\n"
            "- duplicated package or module name taking precedence in "
            "sys.path;\n"
            "- missing module, class, function or variable;\n\n"
            "Debugged import:\n\n%s\n\n"
            "Original exception:\n\n%s: %s"
        )

        name = ""
        tracked = []
        for part in import_name.replace(":", ".").split("."):
            name += (name and ".") + part
            imported = import_string(name, silent=True)
            if imported:
                tracked.append((name, getattr(imported, "__file__", None)))
            else:
                track = ["- %r found in %r." % (n, i) for n, i in tracked]
                track.append("- %r not found." % name)
                msg = msg % (
                    import_name,
                    "\n".join(track),
                    exception.__class__.__name__,
                    str(exception),
                )
                break

        ImportError.__init__(self, msg)

    def __repr__(self):
        return "<%s(%r, %r)>" % (
            self.__class__.__name__,
            self.import_name,
            self.exception,
        )


def reraise(tp, value, tb=None):
    """ Reraises an error.

    Copied from the werkzeug library, which is BSD-3 licensed.
    """
    if value.__traceback__ is not tb:
        raise value.with_traceback(tb)
    raise value


def import_string(import_name, silent=False):
    """Imports an object based on a string.  This is useful if you want to
    use import paths as endpoints or something similar.  An import path can
    be specified either in dotted notation (``xml.sax.saxutils.escape``)
    or with a colon as object delimiter (``xml.sax.saxutils:escape``).

    If `silent` is True the return value will be `None` if the import fails.

    :param import_name: the dotted name for the object to import.
    :param silent: if set to `True` import errors are ignored and
                   `None` is returned instead.
    :return: imported object

    Copied from the werkzeug library, which is BSD-3 licensed.
    """
    # force the import name to automatically convert to strings
    # __import__ is not able to handle unicode strings in the fromlist
    # if the module is a package
    import_name = str(import_name).replace(":", ".")
    try:
        try:
            __import__(import_name)
        except ImportError:
            if "." not in import_name:
                raise
        else:
            return sys.modules[import_name]

        module_name, obj_name = import_name.rsplit(".", 1)
        module = __import__(module_name, globals(), locals(), [obj_name])
        try:
            return getattr(module, obj_name)
        except AttributeError as e:
            raise ImportError(e)

    except ImportError as e:
        if not silent:
            reraise(
                ImportStringError, ImportStringError(import_name, e), sys.exc_info()[2]
            )
