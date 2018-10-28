#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
An abstract class that is an observer of our server and is notified to events.
This will be extended by all modules of this bot.

Default behaviors are to just return
"""

from abc import ABC, abstractmethod


class TeamBotModule(ABC):

    '''
    Notifies about a message in a channel
    '''
    @abstractmethod
    def notifyMessage(self, teamRTM, message):
        return

    '''
    Notifies that a reaction was added to a message
    '''
    @abstractmethod
    def notifyReaction(self, teamRTM, reaction):
        return

    '''
    Notifies channel history was changed
    '''
    @abstractmethod
    def notifyChannelHistoryChange(self, teamRTM, channelHistoryChange):
        return

    '''
    Notifies on presence change of a user
    '''
    @abstractmethod
    def notifyPresenceChange(self, teamRTM, presenceChange):
        return

