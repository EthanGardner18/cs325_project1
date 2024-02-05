Project 1 - CS325 Ethan Gardner

Description:
This is a Python program used to scrape and save articles from a given url.

Steps to run my program.

First install Anaconda on your device:

    1. Go to https://www.anaconda.com to download the latest version of Anaconda to your device. 
    2. After instalation check to see if it downloaded correctly by typing conda activate into you command prompt

Next clone the repository

    1. Copy the link by hitting the green code button(make sure you click on the https option)
    2. Now go to the command promt and type: git clone "link"

Setup Conda Environment

    1. Still in the command prompt type conda env create --name "environment name you want" -- file=requirements.yaml
    2. Then type the command conda activate "the name of your environment" (if you dont remember the name type: conda env list)

Running the program

    1. Still in the command prompt type python main.py imput.txt
    2. This will create the 5 files
    3. type cat "File Name" to see what was scraped and saved. 
