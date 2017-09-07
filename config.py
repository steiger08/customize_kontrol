class Config:
    def __init__(self, data = []):
        self.instrument_list = data

    def add_instrument(self, instrument):
        self.instrument_list += {instrument}

    def data(self):
        return self.instrument_list
    
