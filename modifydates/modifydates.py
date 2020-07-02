from datetime import datetime as dt
import QuantLib as ql


def datetimeToQuantLib(d):
    """
    Transforms a datetime date to a QuantLib Date object
    """
    return ql.Date(d.day, d.month, d.year)


def dateToQuantLib(d):
    """
    Transforms a date in format dd/mm/yyyy to a QuantLib Date object
    """
    x = dt.strptime(d, "%d/%m/%Y")
    return ql.Date(x.day, x.month, x.year)


def quantLibToDate(d):
    """
    Transforms a QuantLib Date object to a date in format dd/mm/yyyy
    """
    return(str(d.dayOfMonth()).zfill(2) + '/' + str(d.month()).zfill(2) + '/' + str(d.year()))
