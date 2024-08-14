import os
import json
from dotenv import load_dotenv
from URL_to_markdown import URL_to_markdown

load_dotenv("chatbot/.env")

#key
JINA_TOKEN = os.environ.get("JINA_TOKEN")


def json_to_markdown(json_files_dir,wxid):
    """
    遍历目录下的所有JSON文件,获取URL,调用URL_to_markdown(),
    json_files_dir 文件路径
    """
    for filename in os.listdir(json_files_dir):  # 遍历文件夹下json文件

        if filename.endswith(".json"):
            print(filename.endswith(".json"))

            file_path = os.path.join(json_files_dir, filename)
        
            # 读取JSON文件
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        
            # 获取URL
            art_url = data.get('art_url', None)

            # 检查art_url是否不是None，并且以'http://'开头
            if art_url and art_url.lower().startswith('http://'):
             # 替换'http://'为'https://'
                art_url = 'https://' + art_url[7:]

            # 输出修改后的URL

            title1 = data.get('title', 'Untitled')

            # URL保存为Markdown
            try:
                URL_to_markdown(art_url,wxid,title1,JINA_TOKEN)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                continue

        else:
            print(f"No art_url found in {filename}")


    



