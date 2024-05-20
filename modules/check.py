import platform



def system():
    if platform.system().lower() == "windows":
        return "windows"
    elif platform.system().lower() == "linux":
        return "linux"
    elif platform.system().lower() == "darwin":
        return "darwin"
    else:
        return "android"
