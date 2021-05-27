from shop import getShop, makeImage
import json

with open('./config.json') as f:
  config = json.load(f)
  shop = getShop(config['auth'])
  makeImage(shop, config['ad1'], config['ad2'], config['saveFileLocation'])