from mycroft import MycroftSkill, intent_file_handler

from .merry import be_merry


class ChristmasTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.christmas.intent')
    def handle_test_christmas(self, message):
        self.speak_dialog('test.christmas')
        my_msg = be_merry()
        self.speak(my_msg)


def create_skill():
    return ChristmasTest()

