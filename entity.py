import inspect

class Entity(object):
    def __getitem__(self, key):
        return self.__dict__[key] 

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def pack(self):
        d = dict()
        for attr, value in self.__dict__.iteritems():
            if not inspect.ismethod(value):
                d[attr] = value
        return d

    def unpack(self, d):
        for key, value in d:
            self.__dict__[key] = value
