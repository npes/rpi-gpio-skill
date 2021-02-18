from mycroft import MycroftSkill, intent_file_handler


class RpiGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gpio.rpi.intent')
    def handle_gpio_rpi(self, message):
        self.speak_dialog('gpio.rpi')


def create_skill():
    return RpiGpio()

