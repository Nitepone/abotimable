"""
    File: ricFlair.py
    Version: 1.0.0
    Author: Chris Baudouin, Jr.

    Description: Anytime "woo" is mentioned in chat, abotimable will post a ric flair picture
"""
import re

def check_for_woo(message):
    match_obj = re.match(r'wo{2,} *', message)

    if match_obj:
        return
    else:
        return


def process_payload(payload):
    return
