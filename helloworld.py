libs = {}
try:
    import requests
    libs['requests'] = True
except:
    libs['requests'] = False
try:
    import urllib
    libs['urllib'] = True
except:
    libs['urllib'] = False
try:
    import httplib2
    libs['httplib2'] = True
except:
    libs['httplib2'] = False

print(libs)
