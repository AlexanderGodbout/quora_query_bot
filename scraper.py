# new file

import requests
import json 


def get_all_subreddits():
    content = requests.get('https://www.reddit.com/reddits.json', headers = {'User-agent': 'your bot 0.1'})
    return json.loads(content.content)

    #with urllib.request.urlopen("http://www.reddit.com/reddits.json") as url:
    #    data = json.loads(url.read().decode())
    #    print(data)

results = get_all_subreddits()


for child in results["data"]['children']: 
    print(child['data']['display_name_prefixed'])
