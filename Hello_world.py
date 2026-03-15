import sys # 导入sys模块以便退出

class HelloWorld:# 定义HelloWorld类

    def hello(self):# 定义hello方法
        sys.stdout.write(f"Hello, world!") # 输出Hello, world!

def main(): # 定义main函数
    hello_world = HelloWorld() # 创建HelloWorld对象
    hello_world.hello() # 调用hello方法

if __name__ == "__main__": # 如果当前模块是主程序
    main() # 调用main函数
    sys.exit() # 退出程序