from get_articals_URL import get_article_urls
import os
from urllib.parse import quote
from dotenv import load_dotenv
from json_to_markdown import json_to_markdown

load_dotenv("chatbot/.env")

#key
WX_TOKEN = os.environ.get("WX_TOKEN")
JINA_TOKEN = os.environ.get("JINA_TOKEN")


if __name__ == "__main__":
    #get_article_urls('chuanjibang', WX_TOKEN, cursor=None)
    json_to_markdown('D:\chatbot\json','chuanjibang')

"""
D:\chatbot\json是保存的文件夹路径,要换成你实际的
"""

