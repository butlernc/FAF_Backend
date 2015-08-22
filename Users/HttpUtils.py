__author__ = 'butlernc'
import httplib


def registerToC2DMServer(email, password):

    GOOGLE_URL = "https://www.google.com/accounts/ClientLogin"

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
