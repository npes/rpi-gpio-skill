from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
from os.path import dirname, abspath
import sys

sys.path.append(abspath(dirname(__file__)))
import GPIO

class RpiGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

       
    # @intent_file_handler('gpio.rpi.intent')
    # def handle_gpio_rpi(self, message):
    #     self.speak_dialog('gpio.rpi')

    def on_led_change(self, gpio_name):
        """used to report the state of the led.
        This is attached to the on change event.  And will speak the
        status of the led.
        """
        if GPIO.get(gpio_name)!="On":
                GPIO.set(gpio_name,"On")
        else:
            GPIO.set(gpio_name,"Off")
        #status = GPIO.get(gpio_name)
        #self.speak("Led is %s" % status)

    @intent_handler(IntentBuilder('GpioIntent').require('pin').require('command'))
    def handle_gpio(self, message):

        pin = message.data.get('pin')
        command = message.data.get('command')

        if command == 'on':
            if pin == 'gpio one':
                #self.speak_dialog('gpio 1 is on')
                self.on_led_change('GPIO1')
            elif pin == 'gpio two':
                self.on_led_change('GPIO2')
            if pin == 'gpio 1':
                self.on_led_change('GPIO1')
            elif pin == 'gpio 2':
                self.on_led_change('GPIO2')

        elif command == 'off':
            if pin == 'gpio one':
                self.on_led_change('GPIO1')
            elif pin == 'gpio two':
                self.on_led_change('GPIO2')
            if pin == 'gpio 1':
                self.on_led_change('GPIO1')
            elif pin == 'gpio 2':
                self.on_led_change('GPIO2')
        else:
            self.speak_dialog('i do not understand you, please try again')


def create_skill():
    return RpiGpio()

