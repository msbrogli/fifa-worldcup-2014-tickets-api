import urllib2
import json

def get_availability(country='BRA'):
    x = urllib2.urlopen('https://fwctickets.fifa.com/TopsAkaCalls/Calls.aspx/getRefreshChartAvaDem?l=en&c={}'.format(country)).read()
    obj = json.loads(x)
    obj2 = json.loads(obj['d']['data'])
    return obj2

def get_availables(country='BRA'):
    obj = get_availability(country)
    v = []
    for x in obj['BasicCodes']['PRODUCTPRICES']:
        if int(x['Quantity']) > 0:
            v.append(x)
    return v

def get_basic_info():
    x = urllib2.urlopen('https://fwctickets.fifa.com/TopsAkaCalls/Calls.aspx/getBasicData?l=en&c=BRA').read()
    obj = json.loads(x)
    obj2 = json.loads(obj['d']['data'])
    return obj2

def get_products():
    obj2 = get_basic_info()
    products = dict([(x['ProductId'], x) for x in obj2['BasicCodes']['PRODUCTS']])
    return products

def get_availables_at_rio():
    avail = get_availables()
    products = get_products()
    v = []
    for x in avail:
        y = products.get(x['PRPProductId'])
        if y['MatchStadium'] == '10':
            v.append((y, x))
            print y, x
            print
    return v
