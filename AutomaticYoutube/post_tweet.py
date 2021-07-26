import os
from os.path import join, dirname
from dotenv import load_dotenv
from twitter_bot_class import TwitterBot
import ffmpeg


if __name__ == "__main__":
    load_dotenv(verbose=True)

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    USN = os.environ.get("USER_NAME")
    PWD = os.environ.get("PASSWORD")
    try:
        pj = TwitterBot(USN, PWD)
        pj.login()
        ffmpeg.input("https://twitter.com/JthKomapi/status/1337610660679569408").output("/Users/mink/Documents/Pythons/AutoMaticYoutube/Movie").run()
        # pj.post_tweets("selenium による自動ツイートテスト")
        pj.logout()
    except Exception as e:
        pj.logout()
        print(e)

