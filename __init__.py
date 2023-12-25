from mycroft import MycroftSkill, intent_file_handler


class ChristmasTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.christmas.intent')
    def handle_test_christmas(self, message):
        self.speak_dialog('test.christmas')


def create_skill():
    return ChristmasTest()

