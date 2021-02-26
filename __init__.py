from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler


class RpiGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gpio1.rpi.intent')
    def handle_gpio_rpi(self, message):
        self.speak_dialog('gpio.rpi')

    @intent_handler(IntentBuilder('GpioIntent').optionally('pin'))
    def handle_gpio(self, message):
        pin = message.data.get('pin')
        if pin == 'gpio one':
            self.speak_dialog('gpio one is on')
        elif pin == 'gpio two':
            self.speak_dialog('gpio two is on')
        elif pin == 'gpio three':
            self.speak_dialog('gpio three is on')


def create_skill():
    return RpiGpio()

