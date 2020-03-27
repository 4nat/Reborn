# My first small module for colored messages! :D

def cprint(color, message):
    if color == "red":
        return print("\033[1;31;40m", message, "\033[1;37;40m")
    elif color == "green":
        return print("\033[1;32;40m", message, "\033[1;37;40m")
    elif color == "yellow":
        return print("\033[1;33;40m", message, "\033[1;37;40m")
    elif color == "blue":
        return print("\033[1;34;40m", message, "\033[1;37;40m")
    elif color == "purple":
        return print("\033[1;35;40m", message, "\033[1;37;40m")
    elif color == "cyan":
        return print("\033[1;36;40m", message, "\033[1;37;40m")
    else:
        return print("\033[1;37;40m", message, "\033[1;37;40m")
