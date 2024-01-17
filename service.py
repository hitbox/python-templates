# - imports sorted starting from the standard library to nearest to this
#   module. Also, `import package` first, then `from package import name`.
# - prefer one import per line, many names on one line are hard to read and manage
# - sorted lexicographically
import argparse
import configparser
import itertools as it # use common abbreviations
import logging.config
import sys
import unittest

# from-imports after import-imports
from itertools import combinations
from itertools import product
from pathlib import Path

# imports from third-party modules

# finally, other modules like ones in this project's repo

# a global "constant" may be worth not having to remember to change it
# everywhere it appears
APPNAME = 'service'

class TestService(unittest.TestCase):
    # easy to run tests with `python -m unittest service.py`

    def test_main(self):
        # - usually not necessary to test the `main` function but sometimes
        #   there's tricky interdependent flags and such.
        # - I always give `main` the argv argument because it's easy and
        #   reminds me that it is prepared to be tested.
        pass

    def test_run(self):
        # - whatever tests to ensure your functions behave
        pass


class ServiceError(Exception):
    """
    An exception raised by this service.
    """


def run(config):
    """
    Description of what this will do.
    """
    # - do whatever real work this service is intended to do
    # - this or another function ought to be something you might call from
    #   other code, if nothing else, so that you can test it
    logger = logging.getLogger(APPNAME)
    logger.info(str(config))
    # - ridiculous exit code for testing this template script works
    exitcode = 99
    return exitcode

def parse_config(cp):
    # - pull and parse whatever is needed out of configuration
    # - in real life this usually requires converting to Python data types
    #   other than str
    section = cp[APPNAME]

    # prefer key access for required keys so that KeyError is raised.
    username = section['username']
    password = section['password']

    # - `.get` or something similar for optionals
    # - also, a dry run flag is usually helpful
    dry = section.getboolean('dry')

    # - return whatever makes sense, dicts are common
    # - often prefer naming what we're returning for clarity
    # - this also puts the return statement on its own line
    config = dict(
        username = username,
        password = password,
        dry = dry,
    )
    return config

def main(argv=None):
    """
    Short description of service invoked by --help
    """
    parser = argparse.ArgumentParser(
        description = main.__doc__,
    )
    parser.add_argument(
        'config',
        nargs = '+',
        help = 'One or more configuration files.',
    )
    args = parser.parse_args(argv)

    # configparser.ExtendedInterpolationParser is useful too
    cp = configparser.ConfigParser()
    cp.read(args.config)

    # configure logging as soon as possible
    if set(['loggers', 'handlers', 'formatters']).issubset(cp):
        logging.config.fileConfig(cp)
    # - make logging configuration a requirement by just calling this or
    #   another function
    # - usually want it optional for development

    config = parse_config(cp)

    # - grab our logger in case there's an exception in `run` or similar
    # - we're getting into the territory where this stuff after `fileConfig` is
    #   application or service specific, so do whatever makes the most sense
    # - probably best to get logger now, so a problem is seen as soon as
    #   possible
    logger = logging.getLogger(APPNAME)

    try:
        # return for exit code if needed
        return run(config)
    except Exception:
        # - the only place to use a catch-all exception handler to alert us of
        #   any exception, usually by a logging.handlers.SMTPHandler
        # - other exception handlers should catch specific errors and handle them
        # - otherwise let exceptions raise, they are very useful and usually
        #   tell you about a major problem
        logger.exception('An exception occured')

if __name__ == '__main__':
    # keep global namespace clean, the only thing that goes inside the
    # main-check is a call to a function or something similar

    # sys.exit for exit code, I often omit
    sys.exit(main())
