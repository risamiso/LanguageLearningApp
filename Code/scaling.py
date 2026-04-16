
#base resolution is: 1920x1080

scale = None


def init(w, h):
    global scale
    scale = max(w / 1920, h / 1080) #pick lower value to avoid anything going outside the screen

def scaleSize(s):
    if scale is None:
        raise Exception("Scale not initialized yet!")
    return int(s * scale)