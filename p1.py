# this project is finding 5 articles from a news website and scraping the words into a text file

# link 1: https://www.foxnews.com/sports/hopeful-bettor-places-100000-wager-super-bowl-coin-toss-tails-never-fails
# link 2: https://www.foxnews.com/sports/ex-nfl-star-jim-mcmahon-recalls-super-bowl-memories-wanted-forget-first-one
# link 3: https://www.foxnews.com/sports/ex-longhorns-star-bijan-robinson-jokingly-agrees-horns-down-taunt-should-come-consequences
# link 4: https://www.foxnews.com/sports/syracuse-legend-jim-boeheim-reveals-hardest-part-basketball-programs-conference-realignment
# link 5: https://www.foxnews.com/sports/taylor-swift-frenzy-great-for-football-former-nfl-stars-say

# My scraper is beautifulsoup

from bs4 import BeautifulSoup
import requests
import json

url1 = "https://www.foxnews.com/sports/hopeful-bettor-places-100000-wager-super-bowl-coin-toss-tails-never-fails"
url2 = "https://www.foxnews.com/sports/ex-nfl-star-jim-mcmahon-recalls-super-bowl-memories-wanted-forget-first-one"
url3 = "https://www.foxnews.com/sports/ex-longhorns-star-bijan-robinson-jokingly-agrees-horns-down-taunt-should-come-consequences"
url4 = "https://www.foxnews.com/sports/syracuse-legend-jim-boeheim-reveals-hardest-part-basketball-programs-conference-realignment"
url5 = "https://www.foxnews.com/sports/taylor-swift-frenzy-great-for-football-former-nfl-stars-say"

result = requests.get(url2)
doc = BeautifulSoup(result.text,"html.parser")

tag = doc.find("script", {"type": "application/ld+json"})

if tag:
    json_data = json.loads(tag.string)
    article_body = json_data.get("articleBody", "")
    print(article_body)
