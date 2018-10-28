"""
FILE: lmgtfy.py
PROJECT: abotimable

When I was somewhere between 10 and 12 years
old, I thought "Let Me Google That For You"
was the funniest thing in the universe. I've
come a long way from those dark times.

Abotimable hasn't.

Bonus points for using AOL instead of Google.

@author Trevor S. (txs6996)
@version 1.0

"""

base_url = "http://lmgtfy.com/?s=a&q="


def buildmessage(channel, text):
    msg = {
        channel: channel,
        text: text
    }


def make_link(question):
    words = question.split(" ")
    link = base_url
    for w in words:
        link += "+" + w

    return link


if __name__ == '__main__':
    incoming = "what is a question?"
    question = incoming.split("?")[0]
    res = make_link(question)
    print(res)
