import requests
import argparse

def check_for_leak(base_url, query_param):
    # 构建请求的URL
    url = f"{base_url}/scrape.php?page=1&q={query_param}"
    
    # 设置请求头部
    headers = {
        'Host': 'onionland.io',
        'Cookie': 'tor=yes',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers'
    }
    
    # 发送GET请求
    response = requests.get(url, headers=headers)
    
    # 检查响应内容
    if "No Result Found" in response.text:
        print(f"{base_url}/search/ 没有信息泄露。")
    else:
        print(f"{base_url}/search/ 可能存在信息泄露。")

def main():
    parser = argparse.ArgumentParser(description="检查网站是否泄露特定查询的信息")
    parser.add_argument("query_param", type=str, help="查询参数")
    args = parser.parse_args()
    
    # 使用示例
    base_url = "http://onionland.io"
    query_param = args.query_param
    check_for_leak(base_url, query_param)

if __name__ == "__main__":
    main()