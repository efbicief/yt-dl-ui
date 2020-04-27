import platform

def get_platform():

    pf = platform.system()

    if pf.lower().startswith("linux"):
        print('Platform "' + pf + '" detected.')
        return 'linux'
    elif pf.lower().startswith("windows"):
        print('Platform "' + pf + '" detected.')
        return 'windows'
    else:
        print('Platform "' + pf + '" not explicitly supported. Proceed with caution.')
        return 'linux'