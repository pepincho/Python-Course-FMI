class TestStruct(object):
    '''Class with predefined attributes for testing'''

    def __init__(self, **kwargs):
        '''Set the available struct attributes'''
        self._kwargs = kwargs

    def __getattr__(self, name):
        '''Return dynamically attributes as defined in the constructor'''
        if name in self._kwargs:
            return self._kwargs[name]
        raise AttributeError("Attribute %s not found." % name)
