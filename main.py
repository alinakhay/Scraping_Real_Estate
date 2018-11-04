from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dollars = []
address = []
dates = []
for num in range(0,20):
  url = str('www.realestate.com.au/sold/in-sydney,+nsw+2000/list-'+str(num))
  r = requests.get('http://'+url)
  data = r.text
  soup = BeautifulSoup(data)
  prc = soup.findAll('span', {'class':'property-price'})
  adr = soup.findAll('h2', {'class':'residential-card__address-heading'})
  date = soup.findAll('span', {'class': 'residential-card__with-comma'})
  for i in adr:
      ad = i.findAll('span', {'class': ""})
      address.append(ad[0].text)
  for i in date:
      dt = i.findAll('span', {'role': 'text'})
      dates.append(dt[0].text)
  for i in prc:
    dollars.append(i.text)
prices = []
for j in dollars:
  s = int(''.join(filter(str.isdigit, j)))
  prices.append(s)


data = {'Adress': address, 'Sold Date': dates, 'Price': prices}
dataframe = pd.DataFrame.from_dict(data)
dataframe.describe()
plt.boxplot(prices)
plt.ylabel('Prices')

plt.hist(prices, normed=True, bins=30)
plt.xlabel('Prices')