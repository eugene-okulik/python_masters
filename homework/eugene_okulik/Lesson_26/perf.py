import requests
from datetime import datetime

for i in range(1, 42):
    start = datetime.now()
    requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')
    end = datetime.now()
    print(f'{i}: {end - start}')
