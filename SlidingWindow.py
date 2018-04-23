import re
import matplotlib.pyplot as plt
import time

with open('case.txt', 'r') as case_file:
    case = case_file.read()
    sentence_list = re.findall(r'#([0-9]*?)#}(.*?){', case)
    for window_size in range(1, 20):
        ave_list = []
        tag_list = []
        for idx in range(len(sentence_list)):
            window = sentence_list[idx:idx + window_size]
            window_total_length = sum(len(s[1]) for s in window)
            window_ave_length = window_total_length / window_size
            ave_list.append(window_ave_length)
            tag_list.append(int(sentence_list[idx][0]) * 30 + 1)
        print(ave_list)
        print(tag_list)
        ave_list = ave_list[0:1000]
        tag_list = tag_list[0:1000]
        plt.gcf().set_size_inches(20, 4.8)
        plt.plot(range(len(ave_list)), ave_list)
        plt.plot(range(len(tag_list)), tag_list)
        plt.ylim(0, 100)
        plt.xlabel('窗口大小：%d' % window_size)
        plt.grid()
        plt.show()
        time.sleep(1)
