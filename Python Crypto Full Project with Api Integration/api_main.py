from fastapi import FastAPI,Request
from pydantic import BaseModel
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional,Dict, List, Any
from fastapi.staticfiles import StaticFiles
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse 
import plotly.express as px
from fastapi import Form

myapp = FastAPI()
templates = Jinja2Templates(directory="templates")
myapp.mount("/static", StaticFiles(directory="."), name="static")

class CryptoData(BaseModel):
    symbol: Optional[str] = None
    bitcoin_data: Optional[float] = None
    ethereum_data: Optional[float] = None
    ripple_data: Optional[float] = None
    return_day_btc: Optional[str] = None
    return_value_btc: Optional[float] = None
    mean_return : Optional[float] = None
    return_day_eth: Optional[str] = None
    return_value_eth: Optional[float] = None
    return_day_xrp: Optional[str] = None
    return_value_xrp: Optional[float] = None
    merged_data: Optional[List[List[float]]] = None
    correlation_matrix: Optional[List[List[float]]] = None


    
    # functions
    # def get_crypto_historical_data(self): 

    #     symbol_list = ["BTC-USD","ETH-USD",'XRP-USD']
    #     for symbol in symbol_list:

    #         url = f"https://finance.yahoo.com/quote/{symbol}/history"

    #         # Use Selenium to load the page and execute JavaScript
    #         driver = webdriver.Chrome()  # Make sure to have the ChromeDriver executable in your PATH
    #         driver.get(url)

    #         # Get the page source after JavaScript has loaded
    #         page_source = driver.page_source
    #         driver.quit()  # Close the browser

    #         # Use BeautifulSoup to parse the page source
    #         soup = bs(page_source, 'html.parser')

    #         historical_data = []

    #         for row in soup.select('table[data-test="historical-prices"] tbody tr'):
    #             columns = row.find_all('td')
    #             date = columns[0].text
    #             open_price = columns[1].text
    #             high = columns[2].text
    #             low = columns[3].text
    #             close = columns[4].text
    #             adj_close = columns[5].text
    #             volume = columns[6].text

    #             data = {
    #                 'Date': date,
    #                 'Open': open_price,
    #                 'High': high,
    #                 'Low': low,
    #                 'Close': close,
    #                 'Adj Close': adj_close,
    #                 'Volume': volume
    #             }

    #             historical_data.append(data)

    #         df = pd.DataFrame(historical_data)

    #         # Replace '-' with NaN in the 'Open' and 'Close' columns
    #         df['Open'].replace('-', float('nan'), inplace=True)
    #         df['Close'].replace('-', float('nan'), inplace=True)

    #         # Remove commas and convert the 'Open' and 'Close' columns to float
    #         df['Open'] = df['Open'].str.replace(',', '').astype(float)
    #         df['Close'] = df['Close'].str.replace(',', '').astype(float)

    #         # Calculate Daily Return
    #         return_col = f'{symbol}return'
    #         df[return_col] = (df['Close'] - df['Open']) / df['Open'] * 100

    #         # Save to CSV
    #         df.to_csv(f'{symbol}_crypto_historical_data.csv', index=False)



    def Daily_Returns_mean(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
         # return round(df['Daily Return'].mean(),3)
         # print(f"your bitcoin (BTC-USD) mean return is {round(self.bitcoin_data['BTC-USDreturn'].mean(),3)}")
         # print(f"your etherum (ETH-USD) mean return is {round(self.ethereum_data['ETH-USDreturn'].mean(),3)}")
         # print(f"your ripple mean return is {round(self.ripple_data['XRP-USDreturn'].mean(),3)}") 
        return {"BTCUSD mean is ":round(self.bitcoin_data['BTC-USDreturn'].mean(),3) 
                , "ETHUSD mean is" :  round(self.ethereum_data['ETH-USDreturn'].mean(),3),
                  "XRPUSD mean is " : round(self.ripple_data['XRP-USDreturn'].mean(),3)}
    def Daily_Returns_median(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        print(f"your bitcoin (BTC-USD) median return is {round(self.bitcoin_data['BTC-USDreturn'].median(),3)}")
        print(f"your etherum (ETH-USD) median return is {round(self.ethereum_data['ETH-USDreturn'].median(),3)}")
        print(f"your ripple median return is {round(self.ripple_data['XRP-USDreturn'].median(),3)}")  
        return {"BTCUSD median is ":round(self.bitcoin_data['BTC-USDreturn'].median(),3) 
                , "ETHUSD median is" :  round(self.ethereum_data['ETH-USDreturn'].median(),3),
                  "XRPUSD median is " : round(self.ripple_data['XRP-USDreturn'].median(),3)}
    def Daily_Returns_std(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        # # return round(df['Daily Return'].mean(),3)
        # print(f"your bitcoin (BTC-USD) std return is {round(self.bitcoin_data['BTC-USDreturn'].std(),3)}")
        # print(f"your etherum (ETH-USD) std return is {round(self.ethereum_data['ETH-USDreturn'].std(),3)}")
        # print(f"your ripple std return is {round(self.ripple_data['XRP-USDreturn'].std(),3)}")  
        return {"BTCUSD std-deviation is ":round(self.bitcoin_data['BTC-USDreturn'].median(),3) 
                , "ETHUSD std-deviation is" :  round(self.ethereum_data['ETH-USDreturn'].median(),3),
                  "XRPUSD std-deviation is " : round(self.ripple_data['XRP-USDreturn'].median(),3)}
    
    def Max_Returns_date(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        self.return_day_btc = self.bitcoin_data.loc[self.bitcoin_data['BTC-USDreturn'].idxmax()]['Date']
        self.return_value_btc = self.bitcoin_data['BTC-USDreturn'].max()
        self.return_day_eth = self.ethereum_data.loc[self.ethereum_data['ETH-USDreturn'].idxmax()]['Date']
        self.return_value_eth = self.ethereum_data['ETH-USDreturn'].max()
        self.return_day_xrp = self.ripple_data.loc[self.ripple_data['XRP-USDreturn'].idxmax()]['Date']
        self.return_value_xrp = self.ripple_data['XRP-USDreturn'].max()
        # print(f"THE DATE FOR MAX BTC RETURN IS {self.max_return_day_btc} AND RETURN IS {self.max_return_value_btc}")
        # print(f"THE DATE FOR MAX ETH RETURN IS {self.max_return_day_eth} AND RETURN IS {self.max_return_value_eth}")
        # print(f"THE DATE FOR MAX XRP RETURN IS {self.max_return_day_xrp} AND RETURN IS {self.max_return_value_xrp}")

        return {"BTC COIN MAX INFO": [self.return_day_btc,self.return_value_btc],
                "ETH COIN MAX INFO": [self.return_day_eth , self.return_value_eth],
                "XRP COIN MAX INFO" : [self.return_day_xrp , self.return_value_xrp]}

    def Min_Returns_date(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        self.return_day_btc = self.bitcoin_data.loc[self.bitcoin_data['BTC-USDreturn'].idxmin()]['Date']
        self.return_value_btc = self.bitcoin_data['BTC-USDreturn'].min()
        self.return_day_eth = self.ethereum_data.loc[self.ethereum_data['ETH-USDreturn'].idxmin()]['Date']
        self.return_value_eth = self.ethereum_data['ETH-USDreturn'].min()
        self.return_day_xrp = self.ripple_data.loc[self.ripple_data['XRP-USDreturn'].idxmin()]['Date']
        self.return_value_xrp = self.ripple_data['XRP-USDreturn'].min()
        # print(f"THE DATE FOR MIN BTC RETURN IS {self.return_day_btc} AND RETURN IS {self.return_value_btc}")
        # print(f"THE DATE FOR MIN ETH RETURN IS {self.return_day_eth} AND RETURN IS {self.return_value_eth}")
        # print(f"THE DATE FOR MIN XRP RETURN IS {self.return_day_xrp} AND RETURN IS {self.return_value_xrp}")
        return {"BTC COIN MIN INFO": [self.return_day_btc,self.return_value_btc],
        "ETH COIN MIN INFO": [self.return_day_eth , self.return_value_eth],
        "XRP COIN MIN INFO" : [self.return_day_xrp , self.return_value_xrp]}
    def Corelation_matrix(self) -> Dict[str, Any]:
        # Assume you have three CSV files with historical data for Bitcoin, Ethereum, and Ripple
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')

        # Merge the data frames based on the 'Date' column
        self.merged_data = pd.merge(self.bitcoin_data[['Date', 'BTC-USDreturn']], self.ethereum_data[['Date', 'ETH-USDreturn']], on='Date', how='inner')
        self.merged_data = pd.merge(self.merged_data, self.ripple_data[['Date', 'XRP-USDreturn']], on='Date', how='inner')

        # Calculate the correlation matrix
        self.correlation_matrix = self.merged_data[['BTC-USDreturn', 'ETH-USDreturn', 'XRP-USDreturn']].corr()

        # Convert the correlation matrix to a dictionary
        correlation_dict = self.correlation_matrix.to_dict()

        # Convert DataFrame columns to lists to avoid Pydantic schema generation error
        for col in self.merged_data.columns:
            if isinstance(self.merged_data[col].iloc[0], pd.Timestamp):
                self.merged_data[col] = self.merged_data[col].dt.strftime('%Y-%m-%d')

        # Convert DataFrame to a list of dictionaries
        merged_data_list = self.merged_data.to_dict(orient="records")

        return correlation_dict
    def plot_historical_prices(self):
        
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')

        plt.figure(figsize=(12, 6))

        plt.plot(self.bitcoin_data['Date'], self.bitcoin_data['BTC-USDreturn'], label='Bitcoin (BTC-USD)')
        plt.plot(self.ethereum_data ['Date'], self.ethereum_data ['ETH-USDreturn'], label='Ethereum (ETH-USD)')
        plt.plot(self.ripple_data['Date'], self.ripple_data['XRP-USDreturn'], label='Ripple (XRP-USD)')

        plt.title('Historical Prices of Cryptocurrencies')
        plt.xlabel('Date')
        plt.ylabel('Returns')
        plt.legend()
        plt.grid(True)
        plt.savefig('bitcoin_plot.png')
    def plot_mean_returns_bar_chart(self):
       
    
        
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        print(self.bitcoin_data['BTC-USDreturn'].mean())
        print(self.ethereum_data['ETH-USDreturn'].mean())
        print(self.ripple_data['XRP-USDreturn'].mean())
        # Merge the data frames based on the 'Date' column
        self.merged_data = pd.merge(self.bitcoin_data[['Date', 'BTC-USDreturn']], self.ethereum_data[['Date', 'ETH-USDreturn']], on='Date', how='inner')
        self.merged_data = pd.merge(self.merged_data, self.ripple_data[['Date', 'XRP-USDreturn']], on='Date', how='inner')

        # Calculate the correlation matrix
        self.mean_return = self.merged_data[['BTC-USDreturn', 'ETH-USDreturn', 'XRP-USDreturn']].mean()

        plt.figure(figsize=(8, 5))

        self.mean_return.plot(kind='bar', color=['blue', 'orange', 'green'])
        plt.title('Mean Returns of Cryptocurrencies')
        plt.xlabel('Cryptocurrency')
        plt.ylabel('Mean Return')
        plt.xticks(rotation=0)
        plt.savefig('static/bar_plot.png') 
    
# @myapp.get("/polt",response_class=HTMLResponse)

# async def read(request : Request):

#     return templates.TemplateResponse("result.html" , {"request" : request})
@myapp.get("/",response_class=HTMLResponse)

async def read(request : Request):
    data = {"msg": "default value"}

    return templates.TemplateResponse("index.html" , {"request" : request ,"data":data })

@myapp.post("/", response_class=HTMLResponse)
async def process_calculation(request: Request, calculationDropdown: str = Form(...)):
    obj = CryptoData()
    if calculationDropdown =="1":
        # obj.get_crypto_historical_data()
        val_polt = False
        data = obj.Daily_Returns_mean()
        return templates.TemplateResponse("index.html", {"request": request, "data":data,"val_polt":val_polt})
    elif calculationDropdown =="2":
        val_polt = False
        data = obj.Daily_Returns_median()
        return templates.TemplateResponse("index.html", {"request": request, "data":data,"val_polt":val_polt})
    elif calculationDropdown =="3":
        val_polt = False
        data = obj.Daily_Returns_std() 
        return templates.TemplateResponse("index.html", {"request": request, "data":data,"val_polt":val_polt})     
    elif calculationDropdown =="4":
        val_polt = False
        data = obj.Max_Returns_date()
        return templates.TemplateResponse("index.html", {"request": request, "data":data,"val_polt":val_polt})
    elif calculationDropdown =="5":
        val_polt = False
        data = obj.Min_Returns_date()
        return templates.TemplateResponse("index.html", {"request": request, "data":data,"val_polt":val_polt})
    elif calculationDropdown =="6":
        val_polt = False
        data = obj.Corelation_matrix()   
        return templates.TemplateResponse("index.html", {"request": request, "data":data,"val_polt":val_polt})
    elif calculationDropdown == '7':
        obj.plot_historical_prices()
        data = obj.Corelation_matrix()
        val_polt = True
        his = True
        return templates.TemplateResponse("index.html", {"request": request, "data":data,"val_polt":val_polt,"his":his})
    elif calculationDropdown == '8':
        obj.plot_mean_returns_bar_chart()
        data = obj.Corelation_matrix()
        his = False
        val_polt = True
        return templates.TemplateResponse("index.html", {"request": request, "data":data,"val_polt":val_polt,"his":his})



# @myapp.post("/", response_class=HTMLResponse)
# async def process_calculation(request: Request, calculationDropdown: str = Form(...)):
#     result = {"msg": f"Received POST request with calculationDropdown: {calculationDropdown}"}
#     return templates.TemplateResponse("index.html", {"request": request, "result": result})

# @myapp.post("/", response_class=HTMLResponse)
# async def process_calculation(request: Request, calculationDropdown: str = Form(...)):
#     result = {"msg": f"Received POST request with calculationDropdown: {calculationDropdown}"}
#     return templates.TemplateResponse("index.html", {"request": request, "result": result})
