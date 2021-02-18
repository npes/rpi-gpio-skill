from mycroft import MycroftSkill, intent_file_handler


class RpiGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gpio1.rpi.intent')
    def handle_gpio1_rpi(self, message):
        self.speak_dialog('gpio1.rpi')

    @intent_file_handler('gpio2.rpi.intent')
    def handle_gpio2_rpi(self, message):
        self.speak_dialog('gpio2.rpi')


def create_skill():
    return RpiGpio()

