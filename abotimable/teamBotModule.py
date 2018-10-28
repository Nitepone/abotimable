#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
An abstract class that is an observer of our server and is notified to events.
This will be extended by all modules of this bot.

Default behaviors are to just return
"""

from abc import ABC


class teamBotModule(ABC):

    '''
    Notifies about a message in a channel
    '''
    @abstractmethod
    def notifyMessage(teamRTM, message):
        return


    '''
    Notifies that a reaction was added to a message
    '''
    @abstractmethod
    def notify(teamRTM, reaction):
        return