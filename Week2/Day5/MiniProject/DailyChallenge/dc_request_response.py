import requests
import time

def get_load_time(url):
    start_time = time.time()
    resp = requests.get(url)
    end_time = time.time()
    return end_time - start_time, resp

def test_load_time():
    sites = ['https://www.google.com', 'http://www.ynet.co.il', 'http://www.imdb.com', 'https://developers.institute/']
    for site in sites:
        load_time, resp = get_load_time(site)
        print(f"{site}: {load_time:.2f} seconds")
        print("Response is ", resp)

if __name__ == "__main__":
    test_load_time()
