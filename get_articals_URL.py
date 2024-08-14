import requests
import json
import time
from urllib.parse import quote
from dotenv import load_dotenv
import pandas as pd


def get_article_urls(wxid, key, cursor=None):
    """
    获取文章URL
    """
    url = "http://111.67.193.171:8081/weixin/getps"
    # 请求头
    params = {
        "key": key,
        "wxid": wxid,
        "cursor": cursor,
    }

    # 发送请求
    try:
        response = requests.get(url, params=params)

        # 打印状态码
        # print(response.status_code)

        if response.status_code == 200:  # 检查状态响应码
            data = response.json()
            articles = data["data"]["list"]
            time.sleep(1)
            if data["code"] == 0:  # 为0表示请求成功
                for article in articles:

                    # 打印文章信息
                    title = article.get("title")
                    pub_time = article.get("pub_time")
                    art_url = article.get("art_url")
                    pic_url = article.get("pic_url")
                    cursor = data.get("data").get("cursor")

                    print(
                        f"pub time: {pub_time}, title: {title}, art url: {art_url}, pic url: {pic_url}"
                    )

                    art_data = {
                        "title": title,
                        "pub_time": pub_time,
                        "art_url": art_url,
                        "pic_url": pic_url,
                        "cursor": cursor,
                    }

                    datas = [art_data]  # 放入列表中
                    df = pd.DataFrame(datas)
                    df.to_csv(
                        "articles.csv", mode="a", index=False, header=0
                    )  # 保存为csv文件

                    # 保存文章信息
                    # article_filename = f"{article['title']}.json"
                    # TODO: 若不同公众号的文章title一致怎么办？
                    article_filename = f"D:\\chatbot\\json\\{article['title']}.json"

                    save_article_as_json(article, article_filename)
                    # 文章分割线
                    print("-" * 50)

                if cursor:  # 如果存在游标，表示还有文章
                    get_article_urls(
                        wxid, key, cursor
                    )  # 递归调用自身，新游标获取下一页数据 有没有办法标记游标
            else:
                print(f"Error: {data['msg']}")  # 不为0 打印错误信息
        else:
            print(
                f"Failed to retrieve data from the server, the status code is {response.status_code}"
            )  # 状态码不是200  打印错误信息

    except Exception as e:
        print(f"An error occurred: {e}")
        # TODO: 将当前错误的cursor进行保存，从而断点继续分析


def save_article_as_json(article, article_filename):
    """保存为json"""
    with open(article_filename, "w", encoding="utf-8") as f:
        json.dump(
            {
                "pub_time": article["pub_time"],
                "title": article["title"],
                "art_url": article["art_url"],
                "pic_url": article["pic_url"],
            },
            f,
            ensure_ascii=False,
            indent=4,
        )
    print(f"Saved {article_filename}")


"""
# 示例使用
if __name__ == "__main__":
    wxid = "chuanjibang"  #公众号ID
    key=WX_TOKEN    #TOKEN
    try:
        articles = get_article_urls(wxid,key)
        #time.sleep(5)  #设置请求时间不过于频繁
        # 输出所有获取的文章信息
    except Exception as e:
        # 捕获在主函数中可能出现的任何其他异常
        print(f"An error occurred: {e}")
"""
