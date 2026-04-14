from binance.client import Client

def place_futures_order(client, symbol, side, order_type, quantity, price=None):
    params = {
        'symbol': symbol,
        'side': side,
        'type': order_type,
        'quantity': quantity,
    }
    
    if order_type == 'LIMIT' and price:
        params['price'] = str(price)
        params['timeInForce'] = 'GTC'

    # Futures market mein order place karna
    return client.futures_create_order(**params)