__author__ = 'butlernc'
import httplib


def registerToC2DMServer(email, password):

    SERVER_API_KEY = "AIzaSyAM3SMMv-3CpEnqfmS9g5L9924_vEyVrJg"

    GOOGLE_URL = "gps_request_serializer"

    httpServ = httplib.HTTPConnection(GOOGLE_URL, 80)
    httpServ.connect()

    param_email = "Email=%s" % email
    param_password = "&Passwd=%s" % password
    account_type = "&accountType=GOOGLE"
    source = "&source=Server"
    service = "&service=ac2dm"

    httpServ.request('POST', '/cgi_form.cgi', param_email + param_password + account_type + source + service)
    response = httpServ.getresponse()
    print response
