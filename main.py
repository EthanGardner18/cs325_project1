# this project is finding 5 articles from a news website and scraping the words into a text file

# link 1: https://www.foxnews.com/sports/hopeful-bettor-places-100000-wager-super-bowl-coin-toss-tails-never-fails
# link 2: https://www.foxnews.com/sports/ex-nfl-star-jim-mcmahon-recalls-super-bowl-memories-wanted-forget-first-one
# link 3: https://www.foxnews.com/sports/ex-longhorns-star-bijan-robinson-jokingly-agrees-horns-down-taunt-should-come-consequences
# link 4: https://www.foxnews.com/sports/syracuse-legend-jim-boeheim-reveals-hardest-part-basketball-programs-conference-realignment
# link 5: https://www.foxnews.com/sports/taylor-swift-frenzy-great-for-football-former-nfl-stars-say

# My scraper is beautifulsoup

import argparse
from bs4 import BeautifulSoup
import requests
import json

def getWords(temp):
    result = requests.get(temp)
    doc = BeautifulSoup(result.text, "html.parser")
    
    tag = doc.find("script", {"type": "application/ld+json"})
    
    if tag:
        json_data = json.loads(tag.string)
        article_body = json_data.get("articleBody", "")
        return article_body

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        urls = [line.strip() for line in file.readlines()]

    for idx, url in enumerate(urls, start=1):
        article_body = getWords(url)

        if article_body:
            with open(f"article_{idx}.txt", "w", encoding="utf-8") as file:
                file.write(article_body)

if __name__ == "__main__":
    main()
