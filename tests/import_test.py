#!/usr/bin/env python3.7
import logging
if __name__ == "__main__": logging.basicConfig(level=logging.INFO)

logging.info("Importing models...")
import abotimable.model.message
import abotimable.model.bot
import abotimable.model.channelEvents
import abotimable.model.channelHistoryChange
import abotimable.model.presenseChange
import abotimable.model.reaction

logging.info("Importing team bot modules...")
import abotimable.teamBotModule
import abotimable.testmodule
import abotimable.remindMention
import abotimable.ricFlair
import abotimable.grammar
import abotimable.emotionmodule
import abotimable.songLyrics
import abotimable.superiorOS

logging.info("Importing other modules...")
import abotimable.server
import abotimable.slackrtm

logging.info("Done imports.")
