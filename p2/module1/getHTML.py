# getHTML is the part that uses the parser and requests to actually go to the urls and get
# the data from the url. Then it stores them in the data/raw and labels them as raw1.txt ... 
# the inputs expected are the urls and the outputs are the raw

import argparse
from bs4 import BeautifulSoup
import requests
import json
import os

class Scraper:
    def __init__(self):
        pass

    def get_words(self, temp):
        result = requests.get(temp)
        doc = BeautifulSoup(result.text, "html.parser")
        
        tag = doc.find("script", {"type": "application/ld+json"})
        
        if tag:
            json_data = json.loads(tag.string)
            article_body = json_data.get("articleBody", "")
            return article_body

    def read_urls_from_file(self, input_file):
        with open(input_file, "r") as file:
            urls = [line.strip() for line in file.readlines()]
        return urls

    def write_data_to_files(self, urls, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        
        for idx, url in enumerate(urls, start=1):
            article_body = self.get_words(url)
            if article_body:
                with open(os.path.join(output_dir, f"raw{idx}.txt"), "w", encoding="utf-8") as file:
                    file.write(article_body)

    def scrape(self, input_file):
        urls = self.read_urls_from_file(input_file)
        output_dir = "Data/Raw"
        self.write_data_to_files(urls, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()
    
    scraper = Scraper()
    scraper.scrape(args.input_file)
