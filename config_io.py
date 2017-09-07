import json
import config

class ConfigIO:

    def __init__(self, config_storage_path = ""):
        self.path = config_storage_path
    
    def store(self, config, filename):

        file = open(self.path + filename, "w")
        out_string = json.dumps(config.data())
        file.write(str(out_string))
        file.close
        
        print("Configuration stored successfully to " + str(filename))

    def restore(self, filename):
        file = open(self.path + filename, "r")
        in_string = file.read()
        config = json.loads(in_string)
        file.close

        print("Configuration restored successfully from " + str(filename))
        return config
