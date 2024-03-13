# This is the main file that calls the functions needed to do scraping and formating
# No input is needed in run.py, and run.py doesn't have any actual input itself.

# While coding the modules I used the single responsiblity princlipe, this lets me split the problem into smaller problems
# which makes it easier to test and add more functionality later. Each functions/class has its own small part that it is responsible for
# this makes it more maintainable and scaleable. Note I chose to leave it as a single class with many functions inside it because there 
# really wasn't a need to make a bunch of different classes. The problems were able to be broken down with 2-4 functions easily. 

from module1.getHTML import Scraper
from module2.processData import formatFiles

class Application:
    def __init__(self):
        pass

    def run(self):
        # Scraping data
        scraper = Scraper()
        scraper.scrape("urls.txt")
        
        # Processing data
        input_dir = "Data/Raw"
        output_dir = "Data/Processed"
        formatFiles(input_dir, output_dir)

if __name__ == "__main__":
    app = Application()
    app.run()
