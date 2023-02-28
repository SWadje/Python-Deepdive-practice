class Stock:
    def __init__(self, symbol, date_, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date_
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        
    def as_dict(self):
        return dict(symbol=self.symbol, 
                    date=self.date,
                    open=self.open,
                    high=self.high,
                    low=self.low,
                    close=self.close,
                    volume=self.volume)
        
class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume
        
    def as_dict(self):
        return dict(
            symbol=self.symbol,
            timestamp=self.timestamp,
            order=self.order,
            price=self.price,
            volume=self.volume,
            commission=self.commission)

from datetime import date, datetime
from decimal import Decimal

activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), 
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), 
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), 
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}

from json import JSONEncoder, dumps

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock) or isinstance(obj, Trade):
            return obj.as_dict()
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            super().default(obj)

encoded = dumps(activity, cls=CustomEncoder, indent=2)
print(encoded)

def decode_stock(d):
    s = Stock(d['symbol'], 
              datetime.strptime(d['date'], '%Y-%m-%d').date(), 
              Decimal(d['open']), 
              Decimal(d['high']), 
              Decimal(d['low']), 
              Decimal(d['close']),
              int(d['volume']))
    return s

s = decode_stock({
      "symbol": "AAPL",
      "date": "2018-11-22",
      "open": "176.66",
      "high": "177.25",
      "low": "176.64",
      "close": "176.78",
      "volume": 3699184,
      "object": "Stock"
    })

def decode_trade(d):
    s = Trade(d['symbol'], 
              datetime.strptime(d['timestamp'], '%Y-%m-%dT%H:%M:%S'), 
              d['order'], 
              Decimal(d['price']), 
              int(d['volume']), 
              Decimal(d['commission']))
    return s

t = decode_trade({
      "symbol": "TSLA",
      "timestamp": "2018-11-22T10:05:12",
      "order": "buy",
      "price": "338.25",
      "volume": 100,
      "commission": "9.99",
      "object": "Trade"
    })

type(t), vars(t)

def decode_financials(d):
    object_type = d.get('object', None)
    if object_type == 'Stock':
        return decode_stock(d)
    elif object_type == 'Trade':
        return decode_trade(d)
    return d 

decode_financials({
      "symbol": "TSLA",
      "timestamp": "2018-11-22T10:05:12",
      "order": "buy",
      "price": "338.25",
      "volume": 100,
      "commission": "9.99",
      "object": "Trade"
    })

decode_financials({
      "symbol": "AAPL",
      "date": "2018-11-22",
      "open": "176.66",
      "high": "177.25",
      "low": "176.64",
      "close": "176.78",
      "volume": 3699184,
      "object": "Stock"
    })

from json import JSONDecoder, loads
class CustomDecoder(JSONDecoder):
    def decode(self, arg):
        data = loads(arg)
        # now we have to recursively look for `Trade` and `Stock` objects
        return self.parse_financials(data)
 
    def parse_financials(self, obj):
        if isinstance(obj, dict):
            obj = decode_financials(obj)
            if isinstance(obj, dict):
                for key, value in obj.items():
                    obj[key] = self.parse_financials(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.parse_financials(item)
        return obj

encoded = dumps(activity, cls=CustomEncoder)
print(encoded)
decoded = loads(encoded, cls=CustomDecoder)
print(decoded)

from marshmallow import Schema, fields

class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal()
    high = fields.Decimal()
    low = fields.Decimal()
    close = fields.Decimal()
    volume = fields.Integer()

StockSchema().dump(Stock('TSLA', date(2018, 11, 22), 
                          Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), 
                          Decimal('338.19'), 365_607))

class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    commission = fields.Decimal(as_string=True)
    volume = fields.Integer()

TradeSchema().dumps(Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99'))).data

class ActivitySchema(Schema):
    trades = fields.Nested(TradeSchema, many=True)
    quotes = fields.Nested(StockSchema, many=True)

result = ActivitySchema().dumps(activity, indent=2).data

