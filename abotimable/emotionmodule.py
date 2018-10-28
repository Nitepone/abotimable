"""
    File: emotionmodule.property
    Version: 1.0
    Author: Tyler Hart

    Description: user user emotions to make sensitive responses
"""
from .teamBotModule import TeamBotModule
from watson_developer_cloud import ToneAnalyzerV3
import configparser
import json

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

    def notify_message(sc, message):
        tone = query(message.text)
        if tone["tone_id"] == "sad":
            sc.api_call(
                "reactions.add",
                channel=message.channel,
                name="laughing",
                timestamp=message.ts
            )


TeamBotModule.register(EmotionModule)
