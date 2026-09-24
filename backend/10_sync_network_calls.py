import time
import requests

def main():
    req_count = 10
    url = "https://httpbin.org/get"
    session = requests.Session()
    for i in range(req_count):
        print(f"making request {i}")
        response = session.get(url)
        if response.status_code == 200:
            pass


start = time.time()
main()
end = time.time()
print("Time elapsed: ", end-start)