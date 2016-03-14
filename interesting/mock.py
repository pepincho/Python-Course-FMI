class Mock(object):
    class _MockQuery(object):
        '''Access Mock internals'''

        def __init__(self, mock):
            self._mock = mock

        @property
        def attributes(self):
            return set(self._mock._attrs.keys())

        @property
        def calls(self):
            return tuple(self._mock._calls)

        @property
        def call(self):
            if self._mock._calls:
                return self._mock._calls[-1]

        @property
        def nr_calls(self):
            return len(self._mock._calls)

        @property
        def return_(self):
            return self._mock._return

        @property
        def except_(self):
            return self._mock._except

        @property
        def yield_(self):
            return self._mock._yield_orig

    def __init__(self, return_=None, except_=None, yield_=None, **kwargs):
        self._attrs = kwargs
        self._calls = []
        self._return = return_
        self._except = except_
        self._yield_orig = yield_
        self._yield = iter(yield_) if yield_ else None
        self._qry = self._MockQuery(self)

    def __getattr__(self, value):
        return self._attrs.setdefault(value, Mock())

    def __call__(self, *args, **kwargs):
        self._calls.append((args, kwargs))
        if self._except:
            raise self._except
        if self._yield:
            return self._yield.next()
        if self._return is None:
            self._return = Mock()
        return self._return

    @property
    def qry(self):
        return self._qry
