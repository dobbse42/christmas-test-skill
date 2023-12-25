from mycroft import MycroftSkill, intent_file_handler
#import numpy as np
#import arxiv

from .merry import be_merry, nth_day


class ChristmasTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.christmas.intent')
    def handle_test_christmas(self, message):
        self.speak_dialog('test.christmas')
        my_msg = be_merry()
        my_arr = np.ones(10)
        self.speak(my_msg)
        self.speak(nth_day())


def create_skill():
    return ChristmasTest()

