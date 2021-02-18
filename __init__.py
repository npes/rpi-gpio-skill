from mycroft import MycroftSkill, intent_file_handler


class RpiGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.gpio_Status = [False, False]

    @intent_file_handler('gpio1.rpi.intent')
    def handle_gpio1_rpi(self, message):
        self.speak_dialog('gpio1.rpi')
        if self.gpio_Status [0] == False:
            self.gpio_Status [0] = True
        else:
            self.gpio_Status [0] = False 

    @intent_file_handler('gpio2.rpi.intent')
    def handle_gpio2_rpi(self, message):
        self.speak_dialog('gpio2.rpi')
        if self.gpio_Status [1] == False:
            self.gpio_Status [1] = True
        else:
            self.gpio_Status [1] = False

    @intent_file_handler('gpioStatus.rpi.intent')
    def handle_gpioStatus_rpi(self, message):
        self.speak(f'gpio1 status is{self.gpio_Status[0]} gpio2 status is{self.gpio_Status[1]}')


def create_skill():
    return RpiGpio()

