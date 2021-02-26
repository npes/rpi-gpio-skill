from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler


class RpiGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gpio.rpi.intent')
    def handle_gpio_rpi(self, message):
        self.speak_dialog('gpio.rpi')

    @intent_handler(IntentBuilder('GpioIntent').optionally('pin').optionally('command'))
    def handle_gpio(self, message):
        pin = message.data.get('pin')
        command = message.data.get('command')
        if pin == 'gpio one' or 'gpio 1':
            if command == 'on':
                self.speak_dialog('gpio one is on')
            elif command == 'off':
                self.speak_dialog('gpio one is off')
        elif pin == 'gpio two' or 'gpio 2':
            if command == 'on':
                self.speak_dialog('gpio two is on')
            elif command == 'off':
                self.speak_dialog('gpio two is off')
        elif pin == 'gpio three' or 'gpio 3':
            if command == 'on':
                self.speak_dialog('gpio two is on')
            elif command == 'off':
                self.speak_dialog('gpio two is off')


def create_skill():
    return RpiGpio()

