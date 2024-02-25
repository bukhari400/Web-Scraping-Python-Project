from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot as plt
import os
import plotly.express as px



class CryptoData():

    def get_crypto_historical_data(self, symbol): 
        url = f"https://finance.yahoo.com/quote/{symbol}/history"

        # Use Selenium to load the page and execute JavaScript
        driver = webdriver.Chrome()  # Make sure to have the ChromeDriver executable in your PATH
        driver.get(url)

        # Get the page source after JavaScript has loaded
        page_source = driver.page_source
        driver.quit()  # Close the browser

        # Use BeautifulSoup to parse the page source
        soup = bs(page_source, 'html.parser')

        historical_data = []

        for row in soup.select('table[data-test="historical-prices"] tbody tr'):
            columns = row.find_all('td')
            date = columns[0].text
            open_price = columns[1].text
            high = columns[2].text
            low = columns[3].text
            close = columns[4].text
            adj_close = columns[5].text
            volume = columns[6].text

            data = {
                'Date': date,
                'Open': open_price,
                'High': high,
                'Low': low,
                'Close': close,
                'Adj Close': adj_close,
                'Volume': volume
            }

            historical_data.append(data)

        df = pd.DataFrame(historical_data)

        # Replace '-' with NaN in the 'Open' and 'Close' columns
        df['Open'].replace('-', float('nan'), inplace=True)
        df['Close'].replace('-', float('nan'), inplace=True)

        # Remove commas and convert the 'Open' and 'Close' columns to float
        df['Open'] = df['Open'].str.replace(',', '').astype(float)
        df['Close'] = df['Close'].str.replace(',', '').astype(float)

        # Calculate Daily Return
        return_col = f'{symbol}return'
        df[return_col] = (df['Close'] - df['Open']) / df['Open'] * 100

        # Save to CSV
        df.to_csv(f'{symbol}_crypto_historical_data.csv', index=False)

    
    def Daily_Returns_mean(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        # return round(df['Daily Return'].mean(),3)
        print(f"your bitcoin (BTC-USD) mean return is {round(self.bitcoin_data['BTC-USDreturn'].mean(),3)}")
        print(f"your etherum (ETH-USD) mean return is {round(self.ethereum_data['ETH-USDreturn'].mean(),3)}")
        print(f"your ripple mean return is {round(self.ripple_data['XRP-USDreturn'].mean(),3)}")                                                                                 
    def Daily_Returns_median(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        # return round(df['Daily Return'].mean(),3)
        print(f"your bitcoin (BTC-USD) median return is {round(self.bitcoin_data['BTC-USDreturn'].median(),3)}")
        print(f"your etherum (ETH-USD) median return is {round(self.ethereum_data['ETH-USDreturn'].median(),3)}")
        print(f"your ripple median return is {round(self.ripple_data['XRP-USDreturn'].median(),3)}")  
    def Daily_Returns_std(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        # return round(df['Daily Return'].mean(),3)
        print(f"your bitcoin (BTC-USD) std return is {round(self.bitcoin_data['BTC-USDreturn'].std(),3)}")
        print(f"your etherum (ETH-USD) std return is {round(self.ethereum_data['ETH-USDreturn'].std(),3)}")
        print(f"your ripple std return is {round(self.ripple_data['XRP-USDreturn'].std(),3)}")  
   
   
   
   
   
    def Max_Returns_date(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        self.max_return_day_btc = self.bitcoin_data.loc[self.bitcoin_data['BTC-USDreturn'].idxmax()]['Date']
        self.max_return_value_btc = self.bitcoin_data['BTC-USDreturn'].max()
        self.max_return_day_eth = self.ethereum_data.loc[self.ethereum_data['ETH-USDreturn'].idxmax()]['Date']
        self.max_return_value_eth = self.ethereum_data['ETH-USDreturn'].max()
        self.max_return_day_xrp = self.ripple_data.loc[self.ripple_data['XRP-USDreturn'].idxmax()]['Date']
        self.max_return_value_xrp = self.ripple_data['XRP-USDreturn'].max()
        print(f"THE DATE FOR MAX BTC RETURN IS {self.max_return_day_btc} AND RETURN IS {self.max_return_value_btc}")
        print(f"THE DATE FOR MAX ETH RETURN IS {self.max_return_day_eth} AND RETURN IS {self.max_return_value_eth}")
        print(f"THE DATE FOR MAX XRP RETURN IS {self.max_return_day_xrp} AND RETURN IS {self.max_return_value_xrp}")
    
    
    def Min_Returns_date(self):
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        self.min_return_day_btc = self.bitcoin_data.loc[self.bitcoin_data['BTC-USDreturn'].idxmin()]['Date']
        self.min_return_value_btc = self.bitcoin_data['BTC-USDreturn'].min()
        self.min_return_day_eth = self.ethereum_data.loc[self.ethereum_data['ETH-USDreturn'].idxmin()]['Date']
        self.min_return_value_eth = self.ethereum_data['ETH-USDreturn'].min()
        self.min_return_day_xrp = self.ripple_data.loc[self.ripple_data['XRP-USDreturn'].idxmin()]['Date']
        self.min_return_value_xrp = self.ripple_data['XRP-USDreturn'].min()
        print(f"THE DATE FOR MIN BTC RETURN IS {self.min_return_day_btc} AND RETURN IS {self.min_return_value_btc}")
        print(f"THE DATE FOR MIN ETH RETURN IS {self.min_return_day_eth} AND RETURN IS {self.min_return_value_eth}")
        print(f"THE DATE FOR MIN XRP RETURN IS {self.min_return_day_xrp} AND RETURN IS {self.min_return_value_xrp}")
    def Corelation_matrix(self):
        # Assume you have three CSV files with historical data for Bitcoin, Ethereum, and Ripple
        self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
        self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
        self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
        print()
        # Merge the data frames based on the 'Date' column
        self.merged_data = pd.merge(self.bitcoin_data[['Date', 'BTC-USDreturn']], self.ethereum_data[['Date', 'ETH-USDreturn']], on='Date', how='inner')
        self.merged_data = pd.merge(self.merged_data, self.ripple_data[['Date', 'XRP-USDreturn']], on='Date', how='inner')

        # Calculate the correlation matrix
        self.correlation_matrix = self.merged_data[['BTC-USDreturn', 'ETH-USDreturn', 'XRP-USDreturn']].corr()

        # Print the correlation matrix
        print("Correlation Matrix:")
        print(self.correlation_matrix)  
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
        plt.show()  
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
        plt.show()            


# obj.get_crypto_historical_data(symbol)
# print(obj.Daily_Returns_mean())
# print(obj.Daily_Returns_median())
# print(obj.Daily_Returns_std())
# obj.Max_Returns_date()
# obj.Min_Returns_date()
# obj.Corelation_matrix()
# obj.plot_historical_prices()
# obj.plot_mean_returns_bar_chart()

if __name__ == '__main__':
    obj = CryptoData()
    check_symbol = ['BTC-USD','ETH-USD','XRP-USD']
    while True:
        print("PRESS 1 FOR SCRAP DATA")
        print("PRESS 2 FOR STATISTICAL CALCULATIONS (CONSIDERING A NESTED MENU)")
        print("PRESS 3 POLTING (CONSIDERING A NESTED MENU)")                                                                                                
        choice = input("ENTER YOUR CHOICE BETWEEN 1-3 AND 0 TO QUIT :")
        if choice == '1':
            while True:
                symbol = input("ENTER THE TICKER SYMBOL AND ZERO TO MAIN-MENU ")
                if symbol in check_symbol:
                    obj.get_crypto_historical_data(symbol)
                    break
                elif symbol == "0":
                    break
                else:

                    print("INVALID INPUT ENTER AGAIN")
        elif choice == '2':
            while True:
                print("PRESS 1 FOR MEAN OF TICKER RETURNS")
                print("PRESS 2 FOR MEDIAN OF TICKER RETURNS")
                print("PRESS 3 FOR STD DEV OF TICKER RETURNS")
                print("PRESS 4 FOR MAX RETURE DATE  OF TICKER RETURNS")
                print("PRESS 5 FOR MIN RETURN DATE OF TICKER RETURNS")
                print("PRESS 6 FOR CO REALTION OF MATRIX OF TICKER RETURNS")
                print("PRESS 7 FOR ALL CALCULTIONS OF TICKER RETURNS")
                print("PRESS 0 FOR MAIN-MENU")
                choice_in = input("input your choice ")
                if choice_in == '1':
                    obj.Daily_Returns_mean()
                elif choice_in == '2':
                    obj.Daily_Returns_median()
                elif choice_in == '3':
                    obj.Daily_Returns_std()
                elif choice_in == '4':
                    obj.Max_Returns_date()        
                elif choice_in == '5':
                    obj.Min_Returns_date()
                elif choice_in == '6':
                    obj.Corelation_matrix()
                elif choice_in == '7':
                    print("---------------------------")
                    print(obj.Daily_Returns_mean())
                    print("---------------------------")
                    print(obj.Daily_Returns_median())
                    print("---------------------------")
                    print(obj.Daily_Returns_std())
                    print("---------------------------")
                    obj.Max_Returns_date()
                    print("---------------------------")
                    obj.Min_Returns_date()
                    print("---------------------------")
                    obj.Corelation_matrix()
                    print("---------------------------")
                elif choice_in == '0':
                    break
                else:
                    print('your input in invalid')
                
    
            
        elif choice == '3':
            while True:
                print("PRESS 1 FOR LINE CHART")
                print("PRESS 2 BARCHAT")
                print("PRESS 0 for main menu")
                choice_in = input("input your choice ")
                if choice_in == '1':
                    obj.plot_historical_prices()
                elif choice_in == '2':
                    obj.plot_mean_returns_bar_chart()
                elif choice_in == '0':
                    break
                else:
                    print("invalid output")    


        elif choice == '0':
            break    
        else:
            print("INVALID INPUT")    





