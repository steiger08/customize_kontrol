import config_io
import config

STORAGE_FILENAME = "configuration.sav"
INSTRUMENT_1 = "Klavier 1"
INSTRUMENT_2 = "Klavier 2"

saver = config_io.ConfigIO()
conf_pre = config.Config()
conf_pre.add_instrument(INSTRUMENT_1)
conf_pre.add_instrument(INSTRUMENT_2)
saver.store(conf_pre, STORAGE_FILENAME)

conf_post = config.Config(saver.restore(STORAGE_FILENAME))

print("Config vorher:")
print(conf_pre.data())

print("Config nachher:")
print(conf_post.data())

assert(conf_pre.data() == conf_post.data())

print(" <<<<<<< TEST SUCCESS >>>>>>>")
