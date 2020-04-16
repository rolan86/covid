import os
import json
import requests


if not os.path.exists('data'):
    os.mkdir('data')

base_url = "https://api.covid19api.com/"

def base():
    """
    Gets the data from the base url
    """

    data = {} 
    req = requests.get(base_url)

    if req.status_code == 200:
        data = (json.loads(req.text))

    return data


if __name__ == "__main__":
    print (base())
