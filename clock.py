以下是使用Python语言编写的一个人专注时钟程序代码：

```
import time

def start_timer(minutes):
    print(f'Starting {minutes} minute timer.')
    seconds = minutes * 60
    while seconds > 0:
        print(f'{seconds // 60} : {seconds % 60:02d}')
        time.sleep(1)
        seconds -= 1
    print('Time is up!')

if __name__ == '__main__':
    minutes = int(input('Enter the number of minutes for the timer: '))
    start_timer(minutes)
```

使用方法：

1. 运行程序后，会提示你输入需要专注的时间（单位是分钟）。
2. 程序开始运行后，会按秒倒数并显示剩余时间。
3. 时间到后，程序会提示“Time is up!”。

你可以将代码保存为.py文件，并在命令行中使用python命令运行。如果你想要更友好的界面，可以考虑使用PyQt、Tkinter等GUI库进行界面设计和实现。
