"""
run all the tests

:author: Elliot Miller
:docType: reStructuredText
"""
import logging
import unittest
from .test_style import StyleTest
from .test_import import ImportTest
from .test_bot import BotTest

logging.basicConfig(level=logging.INFO)

unittest.main()
