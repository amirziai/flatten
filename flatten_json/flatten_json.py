def flatten_json(y):
    out = {}

    def flatten(x, name='', delimiter='_'):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + delimiter)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + delimiter)
                i += 1
        else:
            a = ''
            try:
                a = str(x)
            except:
                a = x.encode('ascii', 'ignore').decode('ascii')
            
            out[str(name[:-1])] = a

    flatten(y)
    return out