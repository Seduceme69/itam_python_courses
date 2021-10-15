def debug_control(args):
    a = args.split(", ")
    dick = {'str' : 0, 'int' : 0, 'float' : 0}
    for i in a:
        try:
            i = str(i)
            dick['str'] += 1
            try:
                i = int(i)
                dick['int'] += 1
                dick['str'] -= 1
            except:
                i = float(i)
                dick['float'] += 1
        except:
            pass
    return dick