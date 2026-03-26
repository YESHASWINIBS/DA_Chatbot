cache_store = {}

def check_cache(prompt):
    return cache_store.get(prompt)

def save_cache(prompt, response):
    cache_store[prompt] = response