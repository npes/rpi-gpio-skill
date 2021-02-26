from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler


class RpiGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    # @intent_file_handler('gpio.rpi.intent')
    # def handle_gpio_rpi(self, message):
    #     self.speak_dialog('gpio.rpi')

    @intent_handler(IntentBuilder('GpioIntent').require('pin').require('command'))
    def handle_gpio(self, message):
        pin = message.data.get('pin')
        command = message.data.get('command')
        if command == 'on':
            if pin == 'gpio one':
                self.speak_dialog('gpio 1 is on')
            elif pin == 'gpio two':
                self.speak_dialog('gpio 2 is on')
            elif pin == 'gpio three':
                self.speak_dialog('gpio 3 is on')
            if pin == 'gpio 1':
                self.speak_dialog('gpio 1 is on')
            elif pin == 'gpio 2':
                self.speak_dialog('gpio 2 is on')
            elif pin == 'gpio 3':
                self.speak_dialog('gpio 3 is on')
        elif command == 'off':
            if pin == 'gpio one':
                self.speak_dialog('gpio 1 is off')
            elif pin == 'gpio two':
                self.speak_dialog('gpio 2 is off')
            elif pin == 'gpio three':
                self.speak_dialog('gpio 3 is off')
            if pin == 'gpio 1':
                self.speak_dialog('gpio 1 is off')
            elif pin == 'gpio 2':
                self.speak_dialog('gpio 2 is off')
            elif pin == 'gpio 3':
                self.speak_dialog('gpio 3 is off')
        else:
            self.speak_dialog('i do not understand you, please try again')


def create_skill():
    return RpiGpio()

