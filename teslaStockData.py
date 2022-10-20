# Outputs the tesla stock data 
# Tesla, Inc. :  213.73

import urllib.request, json
resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
data = json.loads(resp.read())
price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
print(data['quoteSummary']['result'][0]['price']['shortName'], ": ", price)
