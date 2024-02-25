from flask import Flask , render_template , request
import requests
app = Flask(__name__)
@app.route("/", methods = ['GET','POST'])
def hello_world():
    major_forex_pairs = ["EURUSD","USDJPY","GBPUSD","USDCHF","USDCAD","AUDUSD","NZDUSD","XAUUSD","XAGUSD","XPTUSD","XPDUSD","WTIUSD","BRENTUSD","NGUSD"]
    pnl=0
    ask_ticker = 0
    temp =0

    if request.method == "POST":
        major_forex_pairs = ["EURUSD","USDJPY","GBPUSD","USDCHF","USDCAD","AUDUSD","NZDUSD","XAUUSD","XAGUSD","XPTUSD","XPDUSD","WTIUSD","BRENTUSD","NGUSD"]
        currencypair = request.form['currencypair']
        temp = currencypair
        tradesize_input = request.form['tradesize']
        openprice_input = request.form['openprice']
        closeprice_input = request.form['closeprice']
        try:
            tradesize = float(tradesize_input)
        except ValueError:
            tradesize = 0

        try:
            openprice = float(openprice_input)
        except ValueError:
            openprice = 0

        try:
            closeprice = float(closeprice_input)
        except ValueError:
            closeprice = 0
        pnl = calculate_pnl(ask_ticker,temp,tradesize,openprice,closeprice)    
    return render_template('index.html', major_forex_pairs = major_forex_pairs,pnl = pnl , ask_ticker = ask_ticker)
def get_ask_price(symbol):
    endpoint = "https://www.alphavantage.co/query"
    
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': 'YOUR_API_KEY',
    }

    try:
        response = requests.get(endpoint, params=params)
        data = response.json()
        
        ask_price = data.get('Global Quote', {}).get('05. price')
        return ask_price
    except Exception as e:
        print(f"Error: {e}")
        return None                                                                                                                     
def calculate_pnl(ask_ticker,temp,tradesize,openprice,closeprice):
    contract_sizes = {
    # Forex Pairs
    "EURUSD": 100000,  # Euro/US Dollar
    "USDJPY": 100000,  # US Dollar/Japanese Yen
    "GBPUSD": 100000,  # British Pound/US Dollar
    "USDCHF": 100000,  # US Dollar/Swiss Franc
    "USDCAD": 100000,  # US Dollar/Canadian Dollar
    "AUDUSD": 100000,  # Australian Dollar/US Dollar
    "NZDUSD": 100000,  # New Zealand Dollar/US Dollar

    # Commodities
    "XAUUSD": 100,     # Gold/US Dollar (per troy ounce)
    "XAGUSD": 5000,    # Silver/US Dollar (per troy ounce)
    "XPTUSD": 50,      # Platinum/US Dollar (per troy ounce)
    "XPDUSD": 100,     # Palladium/US Dollar (per troy ounce)
    "WTIUSD": 1000,    # WTI Crude Oil/US Dollar (per barrel)
    "BRENTUSD": 1000,  # Brent Crude Oil/US Dollar (per barrel)
    "NGUSD": 10000,    # Natural Gas/US Dollar (per mmBtu)
    }
    c = None 
    for symbol,size in contract_sizes.items():
        if symbol == temp:
            c = size
            break
    if c is not None:
        pnl = round((openprice - closeprice) * tradesize * c,2)
        print("Trade Size:", tradesize)
        print("Open Price:", openprice)
        print("Currency Pair:", temp)
        print("Ask Price:", ask_ticker)
        print("Close Price:", closeprice)
        print("Profit and Loss:", pnl)
        print("POST request received")
        return  (openprice - closeprice) * tradesize * c
    else:
        return 0


    

    
app.run(debug =True)    
