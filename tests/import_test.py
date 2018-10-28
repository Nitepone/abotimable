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
import abotimable.model.remindMention
import abotimable.model.ricFlair

logging.info("Importing scripts...")
# import abotimable.server
import abotimable.slackrtm
import abotimable.teamBotModule
import abotimable.testmodule

logging.info("Done imports.")
