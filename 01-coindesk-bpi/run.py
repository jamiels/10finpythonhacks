import requests as r
url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-01-01&end=2021-02-15'
response = r.get(url)
print(response.text)

df = pd.read_json(response.text)
df = df['bpi']
print(df)
df = df.drop(df.tail(2).index)
print(df)