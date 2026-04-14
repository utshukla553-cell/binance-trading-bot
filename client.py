import os
import urllib3
from binance.client import Client
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

def get_binance_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    client = Client(api_key, api_secret, testnet=True)
    client.session.verify = False 
    client.session.timeout = 30 # Timeout 30 seconds
    
    # Alternative Testnet URL try kar rahe hain
    client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
    
    return client