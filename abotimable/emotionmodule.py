"""
    File: emotionmodule.property
    Version: 1.0
    Author: Tyler Hart

    Description: user user emotions to make sensitive responses
"""
import logging
from .teamBotModule import TeamBotModule
from watson_developer_cloud import ToneAnalyzerV3
import configparser
import json
logger = logging.getLogger(__name__)

class EmotionModule():

    def __init__(self):
        config = configparser.RawConfigParser()
        config.read('config.ini')
        capiurl = config['WATSON']['URL']
        cusername = config['WATSON']['USER']
        cpassword = config['WATSON']['PASS']
        self.tone_analyzer = ToneAnalyzerV3(
            version='2018-10-28',
            username=cusername,
            password=cpassword,
            url=capiurl
        )

    def query(self, inputText):
        tone_analysis = self.tone_analyzer.tone(
            {'text':inputText},
            'application/json'
        ).get_result()
        first_tone = tone_analysis["document_tone"]["tones"][0]
        return first_tone

    def notify_message(self, sc, message):
        try:
            tone = self.query(message.text)
        except Exception as e:
            logger.error(e)
            return

        if tone["tone_id"] == "sadness":
            sc.api_call(
                "reactions.add",
                channel=message.channel,
                name="laughing",
                timestamp=message.ts
            )
            logger.info("Tone was sad, message sent")
        else:
            logger.info("Tone was {}, not sad.".format(tone))


TeamBotModule.register(EmotionModule)
