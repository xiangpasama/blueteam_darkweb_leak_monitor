import subprocess
import time

def run_script(script_name, query_param):
    # 构建命令行命令
    command = ["python", script_name, query_param]
    
    # 运行脚本并捕获输出
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # 打印脚本的输出
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)

def main():
    # 定义要运行的脚本列表
    scripts = ["onionland.py", "ahmia.py", "torsearch.py"]
    
    # 定义要传递给脚本的关键词列表
    query_params = ["baidu", "baidukeji"]  # 你可以根据需要添加更多的关键词
    
    # 依次对每个关键词运行每个脚本
    for query_param in query_params:
        print(f"\nQuerying with: {query_param}\n")
        for script in scripts:
            run_script(script, query_param)
            time.sleep(10)  # 暂停10秒

if __name__ == "__main__":
    main()