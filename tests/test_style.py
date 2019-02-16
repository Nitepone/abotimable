"""
Test the style of the code included in this repository

:author: Elliot Miller
:docType: reStructuredText
"""
import os
import unittest
import pycodestyle
import logging

logger = logging.getLogger(__name__)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SEARCH_ROOT = os.path.join(ROOT_DIR, "abotimable")


class StyleTest(unittest.TestCase):

    def test_pep8(self):
        style = pycodestyle.StyleGuide(quiet=False)

        # os.walk is used instead of glob for backwards compatibility
        sources = list()
        for directory, _, filenames in os.walk(SEARCH_ROOT):
            sources.extend(map(
                lambda x: os.path.join(SEARCH_ROOT, directory, x),
                filter(
                    lambda x: x.endswith('.py'),
                    filenames
                )
            ))

        # logs
        logger.info("Found {} source files to check for PEP8"
                    .format(len(sources)))

        # check all source files for PEP8
        result = style.check_files(sources)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
