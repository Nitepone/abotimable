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
from slackclient import SlackClient
from .model.message import Message
from .model.reaction import Reaction
from .model.channelHistoryChange import ChannelHistoryChange
from .model.presenseChange import PresenseChange


class TeamBotModule(ABC):

    '''
    Notifies about a message in a channel
    '''
    @abstractmethod
    def notify_message(self, slack_client: SlackClient,
            message: Message) -> None:
        return

    '''
    Notifies that a reaction was added to a message
    '''
    @abstractmethod
    def notify_reaction(self, team_rtm: SlackClient, reaction: Reaction) -> None:
        return

    '''
    Notifies channel history was changed
    '''
    @abstractmethod
    def notify_channel_history_change(self, team_rtm: SlackClient,
            channel_history_change: ChannelHistoryChange) -> None:
        return

    '''
    Notifies on presence change of a user
    '''
    @abstractmethod
    def notify_presence_change(self, team_rtm: SlackClient,
            presence_change: PresenseChange) -> None:
        return
