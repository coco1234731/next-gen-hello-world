"""Hello, world! 企业版""" # 这个程序的正式名称
import sys # 导入sys模块以便退出
import os # 导入os模块以便退出
import time #导入time模块以便计时, 使用t避免冲突
from datetime import datetime # 导入datetime模块以便保存时间
from datetime import timezone # 导入timezone模块以便计算差值

start = time.perf_counter() # 开始计时

class HelloWorld:# 定义HelloWorld类
    def hello(self):# 定义hello方法
        sys.stdout.write(f"Hello, world!\n") # 输出Hello, world!

def get_time(): # 定义获取时间的函数
    def process(text): # 定义函数，给时间套壳
        process_text = "[" + f"{text}]" # 给时间加上中括号
        return process_text # 返回加上中括号的文本
    utc_now = datetime.now(timezone.utc) # 获取UTC时间
    utc_processed = process(utc_now) # 处理时间
    return utc_processed # 返回获取到的时间

def get_lang(): # 定义获取语言的函数
    language = os.environ.get('LANG', '') # 获取环境变量中的语言
    if "zh" in language: # 如果语言是中文
        return "c" # c是Chinese的缩写，代表中文
    else: #如果语言不是中文
        return "e" # e是English的缩写，代表英文

def check_need_to_get_version():# 定义检查是否需要获取版本的函数
    lang = get_lang()
    if len(sys.argv) > 1 and (sys.argv[1] == "--version" or sys.argv[1] == "-v"): # 如果命令行参数中包含--version或-v
        if lang == "c": #如果语言是中文
            sys.stdout.write(f"史诗级“Hello, world” 正式版 1.0.0（企业版）\n") # 输出版本信息
        else: #如果语言不是中文
            sys.stdout.write(f"Next Gen \"Hello, world!\". Release 1.0.0(Enterprise Edition)\n") # 输出版本信息
        write_log("v") # 成功输出版本号，写入日志，v代表version
        sys.exit(0) # 退出程序

def write_log(kind, text = None): # 定义写入日志函数
    global start # 声明全局变量
    if text is None:# 如果没有报错
        log_file = open("helloworld.log", "w", encoding = "utf-8") # 打开日志文件
        try: # 捕获可能发生的错误
            if kind == "v": # 如果刚才输出了版本号
                log_file.write(get_time() + f"Output version number success. using " + str(time.perf_counter() - start) + r" second") # 写入日志
            else: # 如果刚才输出了Hello, world!
                log_file.write(get_time() + r"Output 'Hello, world!' success. using " + str(time.perf_counter() - start) + f" second") # 写入日志
        finally: # 结束后执行这里的代码
            log_file.close() # 关闭文件
    else: # 如果发生了错误
        log_file = open("helloworld.log", "w", encoding = "utf-8") #打开文件
        try: # 捕获可能发生的错误
            log_file.write(get_time() + f"Output failed, Error:" + str(text) + r". using " + str(time.perf_counter() - start) + r" second") # 写入日志
        finally:
            log_file.close() # 关闭文件
    return 0 # 表示函数正常退出

def main(): # 定义main函数
    check_need_to_get_version() # 检查是否需要获取版本
    hello_world = HelloWorld() # 创建HelloWorld对象
    hello_world.hello() # 调用hello方法
    write_log("d") # 写入日志，d代表default
    return 0 # 返回0，代表主程序结束

if __name__ == "__main__": # 如果当前模块是主程序
    try: # 捕获可能发生的错误
        main() # 调用main函数
        sys.exit(0) # 正常退出程序
    except Exception as error: # 如果出现错误
        write_log("e", error) # 写入日志，e代表error，第二个参数代表错误内容
        sys.exit(1) # 异常退出程序
else: # 如果不是主程序
    pass # 不执行程序
