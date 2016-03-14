class TestCallable(object):
    '''Callable object for testing'''

    def __init__(self, return_=None, except_=None):
        '''Set the return value or exception type'''
        self._return = return_
        self._except = except_
        self._args = None
        self._kwargs = None
        self._counter = 0

    def __call__(self, *args, **kwargs):
        '''Store the call arguments and return value or raise exception'''
        self._args = args
        self._kwargs = kwargs
        self._counter += 1
        if self._except:
            raise self._except
        return self._return

    @property
    def args(self):
        '''Return last call arguments'''
        return self._args

    @property
    def kwargs(self):
        '''Return last call key arguments'''
        return self._kwargs

    @property
    def counter(self):
        '''Return the number of calls'''
        return self._counter

    def get_except(self):
        '''Return the user defined exception'''
        return self._except

    def get_return(self):
        '''Return the user defined return value'''
        return self._return

    def __type__(self):
        return type(self)
