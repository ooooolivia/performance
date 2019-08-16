def m(**kwargs):
    print(None or 'bar')
    print('foo' in kwargs)
    print ('%s' % kwargs['foo'] if 'foo' in kwargs else 'notfoo')
    print ('%s' % kwargs['bar'] or 'notfoo')

m(bar='blee')