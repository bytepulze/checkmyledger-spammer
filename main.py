import requests as rq
import random

def proxy():
    with open("proxies.txt") as f:
        proxies = f.readlines()
    
    proxy = random.choice(proxies).strip()
    return proxy

def lines():
    with open("proxies.txt") as f:
        proxies = f.readlines()

    lines = len(proxies)
    return lines

postData = {
    "word1": "ltcflip on discord",
    "word2": "ltcflip on discord",
    "word3": "ltcflip on discord",
    "word4": "ltcflip on discord",
    "word5": "ltcflip on discord",
    "word6": "ltcflip on discord",
    "word7": "ltcflip on discord",
    "word8": "ltcflip on discord",
    "word9": "ltcflip on discord",
    "word10": "ltcflip on discord",
    "word11": "ltcflip on discord",
    "word12": "ltcflip on discord",
    "word13": "ltcflip on discord",
    "word14": "ltcflip on discord",
    "word15": "ltcflip on discord",
    "word16": "ltcflip on discord",
    "word17": "ltcflip on discord",
    "word18": "ltcflip on discord",
    "word19": "ltcflip on discord",
    "word20": "ltcflip on discord",
    "word21": "ltcflip on discord",
    "word22": "ltcflip on discord",
    "word23": "ltcflip on discord",
    "word24": "ltcflip on discord"
}

def post():
    line_amount = lines()
    for i in range(line_amount):
        url = "https://checkmyledger.com/"
        r = rq.post(url, data=postData, proxy=proxy())
        if(r.status_code != 302):
            print(r.json())

post()
