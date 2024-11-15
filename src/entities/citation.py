class Citation:
    def __init__(self, data):
        # the code below filter the data from the db.
        # it deletes all the key that have no value assosiated with them.
        self.data = dict((k, v) for k, v in data.iteritems()if v is not None)

    def __str__(self):
        return str(self.data)

    def get_entrys(self):
        return self.data.keys()
