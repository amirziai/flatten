def flatten_json(y, s='.'):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + s)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + s)
                i += 1
        else:
            a = ''
            try:
                a = str(x)
            except:
                a = x.encode('ascii', 'ignore').decode('ascii')
            
            out[str(name[:-len(s)])] = a

    flatten(y)
    return out