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
    def notify_message(self, slack_client, message):
        return

    '''
    Notifies that a reaction was added to a message
    '''
    @abstractmethod
    def notify_reaction(self, team_rtm, reaction):
        return

    '''
    Notifies channel history was changed
    '''
    @abstractmethod
    def notify_channel_history_change(self, team_rtm, channel_history_change):
        return

    '''
    Notifies on presence change of a user
    '''
    @abstractmethod
    def notify_presence_change(self, team_rtm, presence_change):
        return
