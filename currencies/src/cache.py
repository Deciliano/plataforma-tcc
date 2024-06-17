import json
from datetime import datetime, timedelta

CACHE_FILE = "exchange_rates_cache.json"

def read_cache():
    try:
        with open(CACHE_FILE, 'r') as f:
            cache = json.load(f)
            cache['last_update'] = datetime.strptime(cache['last_update'], '%Y-%m-%d %H:%M:%S')
            return cache
    except (FileNotFoundError, KeyError, ValueError):
        return None

def write_cache(data):
    data['last_update'] = data['last_update'].strftime('%Y-%m-%d %H:%M:%S')
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f)

def is_cache_valid():
    cache = read_cache()
    if cache:
        last_update = cache['last_update']
        if datetime.now() - last_update < timedelta(days=1):
            return True
    return False