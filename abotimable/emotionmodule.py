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

        alltones = []
        for tone in tone_analysis["document_tone"]["tones"]:
            alltones.append(tone["tone_id"])
        return alltones

    def notify_message(self, sc, message):
        tones = self.query(message.text)
        # catch no tones
        if len(tones) == 0:
            return

        if "sadness" in tones:
            sc.api_call(
                "reactions.add",
                channel=message.channel,
                name="laughing",
                timestamp=message.ts
            )
            # TO-DO add oof reaction
            logger.debug("Tone was sad, message sent")
        elif "anger" in tones:
            sc.api_call(
                "reactions.add",
                channel=message.channel,
                name="baby_bottle",
                timestamp=message.ts
            )
            logger.debug("Tone was angry, message sent")
        elif "joy" in tones:
            sc.api_call(
                "reactions.add",
                channel=message.channel,
                name="thumbsdown",
                timestamp=message.ts
            )
            logger.debug("Tone was joyful, message sent")
        elif "confident" in tones:
            sc.api_call(
                "reactions.add",
                channel=message.channel,
                name="thinking_face",
                timestamp=message.ts
            )
            logger.debug("Tone was confident, message sent")
        else:
            logger.debug("Tone was {}, no reply.".format(tone))


TeamBotModule.register(EmotionModule)
