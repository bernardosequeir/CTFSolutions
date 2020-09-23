def bouncingBall(h, bounce,window):
    if (h > 0) and (bounce > 0 or bounce < 1) and (window < h):
        i = 0
        while h > window:
            i+=1
            h = h * bounce
            if h > window:
                i+=1
        return h    
    return -1        