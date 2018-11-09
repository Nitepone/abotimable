"""
    File: settings.py
    Version: 1.0.0
    Author: Chris Baudouin, Jr.

    Description: A class that contains global variable settings
"""

class Settings:

    annoyance = 0.5  # Annoyance control for abotimable 0 = off; 1 = maximum
    delay = 1  # Delay used to pause abotimable before responding to certain phrases
    quiet_entrance = True  # Announce abotimable's entrance; not recommended for hackathons

    def __init__(self):
        pass


