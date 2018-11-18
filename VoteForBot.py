from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import configparser
import time
import sys
import logging

def getVoteScreenSite(bot_ID):
    return "https://discordbots.org/bot/{}/vote".format(bot_ID)

def main():
    logging.basicConfig(filename="bot.log", filemode='a', format='%(asctime)s | %(levelname)s | %(message)s', level=logging.INFO, datefmt='%y-%m-%d %H:%M:%S')
    startTime = time.time()
    logging.info("Executing...")
    config = configparser.ConfigParser()
    if(len(sys.argv) > 1):
        config.read(sys.argv[1])
    else:
        config.read('config.txt')

    profile_folder_path = config['Settings']['profile_folder_path']
    bot_id = config['Settings']['bot_id']

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir={}".format(profile_folder_path))
    options.add_argument("headless")
    browser = webdriver.Chrome(options=options)

    browser.get(getVoteScreenSite(bot_id))
    
    try:
        uselessVar = browser.find_element_by_id("userloggedin")
    except NoSuchElementException as exception:
        logging.info(exception)
        logging.warning("***You are not logged in. Will try to log you in.***")
        # Try logging in using existing cookies
        browser.get("https://discordbots.org/login")
        time.sleep(5)
        authorizeButton = browser.find_element_by_class_name("primary")
        authorizeButton.click() # Hopefully we're logged in now...
        time.sleep(5)
        browser.get(getVoteScreenSite(bot_id))
    
    vote_button_xpath = config['Developer Settings']['vote_button_xpath']
    button = browser.find_element_by_xpath(vote_button_xpath)
    button.click()
    time.sleep(2)
    logging.info(button.text)

    browser.quit()
    logging.info("Execution time: {} seconds".format(time.time() - startTime))
    sys.exit(0)

if __name__ == "__main__":
    main()


