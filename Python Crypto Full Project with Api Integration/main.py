# from fastapi import FastAPI
# from pydantic import BaseModel
# from selenium import webdriver
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# from typing import Optional,Dict, List, Any
# import os

# app  = FastAPI()
# # here we  can use the /docs to get the swagger ui
# #and we can ue /redoc to get the following to see the alterantive docmentation

# # hence we are create custumze irl using post get delete put method
# class CryptoData(BaseModel):
#     #pardantic datatype intioization
#     choice : int
#     symbol : str
#     bitcoin_data:Optional[None]
#     ethereum_data: Optional[None]
#     ripple_data : Optional[None]
#     return_day_btc: Optional[None]
#     return_value_btc: Optional[None]
#     return_day_eth: Optional[None]
#     return_value_eth: Optional[None]
#     return_day_xrp: Optional[None]
#     return_value_xrp: Optional[None]
#     merged_data: Optional[pd.DataFrame] = None
#     correlation_matrix: Optional[pd.DataFrame] = None


    
#     # functions
#     def Daily_Returns_mean(self):
#         self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
#         self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
#         self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
#          # return round(df['Daily Return'].mean(),3)
#          # print(f"your bitcoin (BTC-USD) mean return is {round(self.bitcoin_data['BTC-USDreturn'].mean(),3)}")
#          # print(f"your etherum (ETH-USD) mean return is {round(self.ethereum_data['ETH-USDreturn'].mean(),3)}")
#          # print(f"your ripple mean return is {round(self.ripple_data['XRP-USDreturn'].mean(),3)}") 
#         return {"BTCUSD mean is ":round(self.bitcoin_data['BTC-USDreturn'].mean(),3) 
#                 , "ETHUSD mean is" :  round(self.ethereum_data['ETH-USDreturn'].mean(),3),
#                   "XRPUSD mean is " : round(self.ripple_data['XRP-USDreturn'].mean(),3)}
#     def Daily_Returns_median(self):
#         self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
#         self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
#         self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
#         print(f"your bitcoin (BTC-USD) median return is {round(self.bitcoin_data['BTC-USDreturn'].median(),3)}")
#         print(f"your etherum (ETH-USD) median return is {round(self.ethereum_data['ETH-USDreturn'].median(),3)}")
#         print(f"your ripple median return is {round(self.ripple_data['XRP-USDreturn'].median(),3)}")  
#         return {"BTCUSD median is ":round(self.bitcoin_data['BTC-USDreturn'].median(),3) 
#                 , "ETHUSD median is" :  round(self.ethereum_data['ETH-USDreturn'].median(),3),
#                   "XRPUSD median is " : round(self.ripple_data['XRP-USDreturn'].median(),3)}
#     def Daily_Returns_std(self):
#         self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
#         self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
#         self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
#         # # return round(df['Daily Return'].mean(),3)
#         # print(f"your bitcoin (BTC-USD) std return is {round(self.bitcoin_data['BTC-USDreturn'].std(),3)}")
#         # print(f"your etherum (ETH-USD) std return is {round(self.ethereum_data['ETH-USDreturn'].std(),3)}")
#         # print(f"your ripple std return is {round(self.ripple_data['XRP-USDreturn'].std(),3)}")  
#         return {"BTCUSD std-deviation is ":round(self.bitcoin_data['BTC-USDreturn'].median(),3) 
#                 , "ETHUSD std-deviation is" :  round(self.ethereum_data['ETH-USDreturn'].median(),3),
#                   "XRPUSD std-deviation is " : round(self.ripple_data['XRP-USDreturn'].median(),3)}
    
#     def Max_Returns_date(self):
#         self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
#         self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
#         self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
#         self.return_day_btc = self.bitcoin_data.loc[self.bitcoin_data['BTC-USDreturn'].idxmax()]['Date']
#         self.return_value_btc = self.bitcoin_data['BTC-USDreturn'].max()
#         self.return_day_eth = self.ethereum_data.loc[self.ethereum_data['ETH-USDreturn'].idxmax()]['Date']
#         self.return_value_eth = self.ethereum_data['ETH-USDreturn'].max()
#         self.return_day_xrp = self.ripple_data.loc[self.ripple_data['XRP-USDreturn'].idxmax()]['Date']
#         self.return_value_xrp = self.ripple_data['XRP-USDreturn'].max()
#         # print(f"THE DATE FOR MAX BTC RETURN IS {self.max_return_day_btc} AND RETURN IS {self.max_return_value_btc}")
#         # print(f"THE DATE FOR MAX ETH RETURN IS {self.max_return_day_eth} AND RETURN IS {self.max_return_value_eth}")
#         # print(f"THE DATE FOR MAX XRP RETURN IS {self.max_return_day_xrp} AND RETURN IS {self.max_return_value_xrp}")

#         return {"BTC COIN MAX INFO": [self.return_day_btc,self.return_value_btc],
#                 "ETH COIN MAX INFO": [self.return_day_eth , self.return_value_eth],
#                 "XRP COIN MAX INFO" : [self.return_day_xrp , self.return_value_xrp]}

#     def Min_Returns_date(self):
#         self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
#         self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
#         self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')
#         self.return_day_btc = self.bitcoin_data.loc[self.bitcoin_data['BTC-USDreturn'].idxmin()]['Date']
#         self.return_value_btc = self.bitcoin_data['BTC-USDreturn'].min()
#         self.return_day_eth = self.ethereum_data.loc[self.ethereum_data['ETH-USDreturn'].idxmin()]['Date']
#         self.return_value_eth = self.ethereum_data['ETH-USDreturn'].min()
#         self.return_day_xrp = self.ripple_data.loc[self.ripple_data['XRP-USDreturn'].idxmin()]['Date']
#         self.return_value_xrp = self.ripple_data['XRP-USDreturn'].min()
#         # print(f"THE DATE FOR MIN BTC RETURN IS {self.return_day_btc} AND RETURN IS {self.return_value_btc}")
#         # print(f"THE DATE FOR MIN ETH RETURN IS {self.return_day_eth} AND RETURN IS {self.return_value_eth}")
#         # print(f"THE DATE FOR MIN XRP RETURN IS {self.return_day_xrp} AND RETURN IS {self.return_value_xrp}")
#         return {"BTC COIN MIN INFO": [self.return_day_btc,self.return_value_btc],
#         "ETH COIN MIN INFO": [self.return_day_eth , self.return_value_eth],
#         "XRP COIN MIN INFO" : [self.return_day_xrp , self.return_value_xrp]}

#     # class Config:
#     #     arbitrary_types_allowed = True
#     #     json_encoders = {
#     #         pd.DataFrame: lambda v: v.to_dict(orient="records"),
#     #     }

#     # def Corelation_matrix(self) -> Dict[str, Any]:
#     #     # Assume you have three CSV files with historical data for Bitcoin, Ethereum, and Ripple
#     #     self.bitcoin_data = pd.read_csv('BTC-USD_crypto_historical_data.csv')
#     #     self.ethereum_data = pd.read_csv('ETH-USD_crypto_historical_data.csv')
#     #     self.ripple_data = pd.read_csv('XRP-USD_crypto_historical_data.csv')

#     #     # Merge the data frames based on the 'Date' column
#     #     self.merged_data = pd.merge(self.bitcoin_data[['Date', 'BTC-USDreturn']], self.ethereum_data[['Date', 'ETH-USDreturn']], on='Date', how='inner')
#     #     self.merged_data = pd.merge(self.merged_data, self.ripple_data[['Date', 'XRP-USDreturn']], on='Date', how='inner')

#     #     # Calculate the correlation matrix
#     #     self.correlation_matrix = self.merged_data[['BTC-USDreturn', 'ETH-USDreturn', 'XRP-USDreturn']].corr()

#     #     # Convert the correlation matrix to a dictionary
#     #     correlation_dict = self.correlation_matrix.to_dict()

#     #     # Convert DataFrame columns to lists to avoid Pydantic schema generation error
#     #     for col in self.merged_data.columns:
#     #         if isinstance(self.merged_data[col].iloc[0], pd.Timestamp):
#     #             self.merged_data[col] = self.merged_data[col].dt.strftime('%Y-%m-%d')

#     #     # Convert DataFrame to a list of dictionaries
#     #     merged_data_list = self.merged_data.to_dict(orient="records")

#     #     return {"correlation_matrix": correlation_dict}

# #front_end instance-----
# @app.post("/")
# async def main_post(object : CryptoData):
#     if object.choice == 1:
#         return object.Daily_Returns_mean()
#     elif object.choice == 2:
#         return object.Daily_Returns_median()
#     elif object.choice ==3 :
#         return object.Daily_Returns_std()
#     elif object.choice == 4:
#         return object.Max_Returns_date()
#     elif object.choice == 5:
#         return object.Min_Returns_date()
#     elif object.choice == 6:
#         # return object.Corelation_matrix()
#         None
      
