#! /usr/bin/env python3

from flask import Flask, jsonify, request
from cache import *
from currencieService import fetch_external_api

app = Flask(__name__)

@app.route('/currencies', methods=['GET'])
def get_exchange_rate():
    if is_cache_valid():
        cache = read_cache()
    else:
        data = fetch_external_api()
        cache = {
            'last_update': datetime.now(),
            'exchange_rates': {
                'BRL_EUR': data['EUR']['ask'],
                'BRL_USD': data['USD']['ask'],
                'BRL_GBP': data['GBP']['ask'],
                'BRL_CNY': data['CNY']['ask'],
            }
        }
        write_cache(cache)
    
    currency = request.args.get('currency')
    if currency:
        return jsonify({currency: cache['exchange_rates'].get(currency, 'Currency not found')}), 200
    else:
        return jsonify(cache), 200
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')