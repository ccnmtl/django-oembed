from __future__ import unicode_literals

from django.test import TestCase
from oembed.core import replace

class OEmbedTests(TestCase):
    fixtures = ['initial_data.json']

    noembed = r"This is text that should not match any regex."
    end = r"There is this great photo at %s"
    start = r"%s is a photo that I like."
    middle = r"There is a movie here: %s and I really like it."
    trailing_comma = r"This is great %s, but it might not work."
    trailing_period = r"I like this photo, located at %s."

    loc = 'https://www.flickr.com/photos/ian_ruotsala/39088280250/'

    embed = '<img src="https://farm5.staticflickr.com/4776/39088280250_01461fee94_n.jpg" alt="living space is shared with this furry little ambush predator"></img>'

    def testNoEmbed(self):
        self.assertEquals(
            replace(self.noembed),
            self.noembed
        )

    def testEnd(self):
        for text in (self.end, self.start, self.middle, self.trailing_comma, self.trailing_period):
            self.assertEqual(
                replace(text % self.loc),
                text % self.embed
            )

    def testManySameEmbeds(self):
        pass
        text = " ".join([self.middle % self.loc] * 100)
        resp = " ".join([self.middle % self.embed] * 100)
        self.assertEqual(replace(text), resp)
