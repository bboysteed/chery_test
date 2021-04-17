import subprocess
import time
from time import sleep

if __name__ == '__main__':
    f = open("package_name.txt", "r")
    print("mission start at ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    for name in f.readlines():
        print(f'\033[32m正在测试软件:{name.strip()}...\033[0m')
        subprocess.run(f"adb shell monkey -p {name.strip()} --pct-syskeys 0 --throttle 100 -v -v -v 10000 >../LOG/{name.strip()}.log",shell=True)
        sleep(3)
    # print(f'\033[32m正在测试软件:{name.strip()}...\033[0m')
    print("mission end at ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # subprocess.run("ls")
