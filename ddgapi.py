import pytest
import collections

import requests

results = []

d = {'q': "presidents of the united states", 'format': 'json'}

r = requests.get('http://api.duckduckgo.com', d)

data = r.json()

topics = data['RelatedTopics']

for x in topics:
    results.append(x['Text'])


def test_presidents():
    presidents = ["Washington", "Jefferson", "Adams", "Madison", "Monroe", "Jackson", "Van Buren", "Harrison", "Tyler",
                  "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes",
                  "Garfield", "Arthur", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge",
                  "Hoover", "Truman", "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton",
                  "Obama", "Trump", "Biden"]
    presidents2 = []
    for y in presidents:
        if any(y in word for word in results):
            presidents2.append(y)
    assert collections.Counter(presidents) == collections.Counter(presidents2)
