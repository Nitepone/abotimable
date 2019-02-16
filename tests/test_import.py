"""
Test that all modules contained within can be imported

:author: Elliot Miller
:docType: reStructuredText
"""
import unittest


class ImportTest(unittest.TestCase):

    def test_models(self):
        import abotimable.model.message
        import abotimable.model.bot
        import abotimable.model.channelEvents
        import abotimable.model.channelHistoryChange
        import abotimable.model.presenseChange
        import abotimable.model.reaction

    def test_modules(self):
        import abotimable.teamBotModule
        import abotimable.testmodule
        import abotimable.remindMention
        import abotimable.ricFlair
        import abotimable.grammar
        import abotimable.emotionmodule
        import abotimable.songLyrics
        import abotimable.superiorOS
        import abotimable.greeter
        import abotimable.lmgtfy

    def test_server(self):
        import abotimable.server

    def test_slackrtm(self):
        import abotimable.slackrtm

if __name__ == "__main__":
    unittest.main()
