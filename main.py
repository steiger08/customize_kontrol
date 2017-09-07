import config
import gui
import config_io
import usb_reader

from threading import Thread

STORAGE_FILENAME = "configuration.sav"

class kontrol_main:
    def __init__(self):

        confIO = config_io.ConfigIO()
        confObj = confIO.restore(STORAGE_FILENAME)
        conf = config.Config(confObj)

        view1 = gui.instrument_view(conf)
        control1 = gui.instrument_controller(view1)

        usb_input = usb_reader.USBReader(control1)

        view1.setup()
        usb_input.run()

kontrol_main()
