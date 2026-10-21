def quote(a):
    t = a * 0.015
    if a > 5000:
        t += 3
    return t
