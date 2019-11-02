import time
def epoch_to_ymd_hms(epoch):
    try:
        if epoch > 9999999999:
            epoch /= 1000
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
    except:
        return ""

def epoch_to_md_hm(epoch):
    try:
        if epoch > 9999999999:
            epoch /= 1000
        return time.strftime('%m-%d %H:%M', time.localtime(epoch))
    except:
        return ""

def epoch_to_yyyymmdd(epoch):
    try:
        if epoch > 9999999999:
            epoch /= 1000
        return time.strftime('%Y%m%d', time.localtime(epoch))
    except:
        return ""

def ms_to_minutes(time_ms):
    return int(time_ms)/1000/60
