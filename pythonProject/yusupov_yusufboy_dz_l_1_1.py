

def convert_time(duration: int) -> int:
    if duration < 60:
        res = str(duration) + 'сек'
    elif duration > 60 and duration < 3600:
        s = duration % 60
        m = duration // 60
        res = str(m) + 'мин ' + str(s) + 'сек'
    elif duration > 3600 and duration < 86400:
        h = duration // 3660
        m = (duration % 3600) // 60
        s = ((duration % 3600) // 60) % 60
        res = str(h) + 'час ' + str(m) + 'мин ' + str(s) + 'сек'
    else:
        d = duration // 86400
        h = (duration % 86400) // 3600
        m = ((duration % 86400) % 3600) // 60
        s = ((duration % 86400) % 3600) % 60
        res = str(d) + ' дн ' + str(h) + ' час ' + str(m) + ' мин ' + str(s) + ' сек '

    return res


duration = input('введите число : ') #400153
result = convert_time(int(duration))
print(result)
duration = input('введите число : ') #400153