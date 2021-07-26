import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from you_get.extractors import tiktok
from Database.get_search_word import TikTok
import random

searchUrl = 'https://www.tiktok.com/tag/{}?lang=ja'
outputDir = '/Users/mink/Documents/Pythons/AutoMaticYoutube/Movie/'
movieXPath = '/html/body/div/div/div[2]/div[2]/div/main/div/div[1]/div[{}]/div/div/div/a'


def main():
    # ブラウザーを起動
    headless = True
    if headless:
        user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
                      ]

        options = webdriver.ChromeOptions()
        options.add_argument(
            '--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
        options = Options()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(
            executable_path=r"/Users/mink/Documents/Pythons/AutoMaticYoutube/chromedriver", options=options)
    else:
        driver = webdriver.Chrome()

    # タグ検索
    tiktok_db = TikTok()
    search_words = tiktok_db.get_words()
    for word in search_words:
        word = word[0]
        driver.get(searchUrl.format(word))
        try:
            os.makedirs("./AutomaticYoutube/Movie/" + word)
        except FileExistsError:
            pass
        time.sleep(3)
        for idx in range(1, 3):
            if idx % 15 == 0:
                # ページの最下部へ移動
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
            try:
                # 動画のXPath取得
                el_a = driver.find_element_by_xpath(
                    movieXPath.format(str(idx)))
            except NoSuchElementException:
                continue

            tiktok.download(el_a.get_attribute('href'),
                            output_dir=outputDir + word, merge=True)

    driver.quit()


if __name__ == "__main__":
    main()
