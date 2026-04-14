import argparse, urllib3, os
from binance.client import Client
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    args = parser.parse_args()

    try:
        # Direct client initialization for submission speed
        client = Client(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_API_SECRET'), testnet=True)
        client.session.verify = False
        client.session.timeout = 60 
        client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        
        print(f"🚀 Sending {args.side} order...")
        res = client.futures_create_order(symbol=args.symbol, side=args.side, type=args.type, quantity=args.quantity)
        print(f"✅ Success! Order ID: {res['orderId']}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()