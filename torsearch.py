import requests
import argparse

def check_for_leak(url, query_param):
    # 构建请求的URL
    params = {'query': query_param}
    
    # 设置请求头部
    headers = {
        'Host': 'torsearch.com',
        'Cookie': 'cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-functional=no; cookielawinfo-checkbox-performance=no; cookielawinfo-checkbox-analytics=no; cookielawinfo-checkbox-advertisement=no; cookielawinfo-checkbox-others=no; _ga_QP8L9RRDET=GS1.1.1726193667.1.0.1726193667.0.0.0; _ga=GA1.1.653157121.1726193667',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
        'Te': 'trailers'
    }
    
    # 发送GET请求
    response = requests.get(url, params=params, headers=headers)

    # 检查响应内容
    if "0 results found" in response.text:
        print(f"{url} 没有信息泄露。")
    else:
        print(f"{url} 可能存在信息泄露。")

def main():
    parser = argparse.ArgumentParser(description="检查网站是否泄露特定查询的信息")
    parser.add_argument("query_param", type=str, help="查询参数")
    args = parser.parse_args()
    
    # 使用示例
    url = "https://torsearch.com/search/"
    query_param = args.query_param
    check_for_leak(url, query_param)

if __name__ == "__main__":
    main()