import requests
import os


def get_output_dir(folder_name):
    """
    定义保存Markdown文件的目录
    folder_name 文件名 即公众号名
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return folder_name


def URL_to_markdown(art_url, wxid, title, key):
    """
    获取到URL后,通过访问jina API存为markdown
    定义请求头,指定返回格式为Markdown
    title:要存为的md文件名 wxid:公众号ID key:Jinatoken
    直接存为了以公众号命名的文件夹
    """
    headers = {
        "Accept": "application/json",
        "Authorization": key,
        "X-Return-Format": "markdown",
    }

    url = f"https://r.jina.ai/{art_url}"

    # 发送请求
    response = requests.post(url, headers=headers)
    # response = requests.post(art_url, headers=headers, data=data)
    # 检查响应状态码
    if response.status_code == 200:
        response_json = response.json()
        print(response_json)

        content = response_json.get("data").get("content")
        # 保存到Markdown文件 文件名为公众号 这里wxid=folder_name
        output_dir = get_output_dir(wxid)
        markdown_file_path = os.path.join(output_dir, f"{title}.md")

        with open(markdown_file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Markdown content for '{title}' saved to {markdown_file_path}")
    else:
        # TODO： 将这些未能解析的URL写入一个文件
        print(
            f"Failed to retrieve Markdown for {art_url}. Status code: {response.status_code}"
        )

    # 输出文章内容
    print(response.text)
