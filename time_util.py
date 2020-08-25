from dateutil.relativedelta import relativedelta
from time import *
from datetime import *

def epoch_to_ymd_hms(epoch):
    try:
        epoch=int(epoch)
        if epoch > 9999999999:
            epoch /= 1000
        return strftime('%Y-%m-%d %H:%M:%S', localtime(epoch))
    except:
        return ""

def epoch_to_md_hm(epoch):
    try:
        epoch=int(epoch)
        if epoch > 9999999999:
            epoch /= 1000
        return strftime('%m-%d %H:%M', localtime(epoch))
    except:
        return ""

def epoch_to_yyyymmdd(epoch):
    try:
        epoch=int(epoch)
        if epoch > 9999999999:
            epoch /= 1000
        return strftime('%Y%m%d', localtime(epoch))
    except:
        print("%s: could not convert epoch %s"%(epoch_to_yyyymmdd.__name__, epoch))
        return ""

def epoch_month_floor(epoch):
    try:
        epoch=int(epoch)
        if epoch > 9999999999:
            epoch /= 1000
        temp = datetime.fromtimestamp(epoch).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        return int(temp.strftime('%s'))
    except:
        print("%s: could not convert epoch %s"%(epoch_month_floor.__name__, epoch))
        return ""

def epoch_to_yyyy_mm_dd(epoch):
    try:
        epoch=int(epoch)
        if epoch > 9999999999:
            epoch /= 1000
        return strftime('%Y_%m_%d', localtime(epoch))
    except:
        print("%s: could not convert epoch %s"%(epoch_to_yyyymmdd.__name__, epoch))
        return ""


def epoch_month_ceil(epoch):
    try:
        epoch=int(epoch)
        if epoch > 9999999999:
            epoch /= 1000
        temp = datetime.fromtimestamp(epoch).replace(day=1, hour=0, minute=0, second=0, microsecond=0) + relativedelta(months=1)
        return int(temp.strftime('%s'))
    except:
        print("%s: could not convert epoch %s"%(epoch_month_ceil.__name__, epoch))
        return ""

def datetime_month_delta(e1, e2):
    try:
        e1 = int(e1)
        e2 = int(e2)
        if e1 > 9999999999:
            e1 /= 1000
        if e2 > 9999999999:
            e2 /= 1000
        e1 = datetime.fromtimestamp(e1)
        e2 = datetime.fromtimestamp(e2)
    except:
        print("%s: could not convert epoch %s %s"%(datetime_month_delta.__name__, e1, e2))
        return ""
    return (e2.year - e1.year) * 12 + e2.month - e1.month


def ms_to_minutes(time_ms):
    return int(time_ms)/1000/60
