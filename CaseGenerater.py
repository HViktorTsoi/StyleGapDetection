import os
import re
import random

prefix = './texts'
file_list = os.listdir(prefix)
print(file_list)
generated_text_list = []
combine_length = 100
sentence_sep = '{#%04d#}'
for file_order, file_name in enumerate(file_list):
    with open('%s/%s' % (prefix, file_name), 'r') as file:
        text = file.read()
        # 过滤字符
        filters = ['\n', ' ', '\u3000', '&nbsp', '“', '”', '「', '」', '\t']
        for f_chr in filters:
            text = text.replace(f_chr, '')
        # 分割句子
        sentences = re.split(r'[。？！]', text)
        print('总句子数 %s' % (len(sentences)))
        for idx in range(len(sentences) // combine_length):
            # 将句子每combine_length句合成一个
            print('正在合成第%s句到第%s句' % (idx * combine_length, (idx + 1) * combine_length))
            combined_text = (sentence_sep % file_order).join(sentences[idx * combine_length:(idx + 1) * combine_length])
            # 在每个定长段落第一句前边也加上分隔符 防止出现长度不一致
            combined_text = "%s%s" % (sentence_sep % file_order, combined_text)
            generated_text_list.append(combined_text)
print(generated_text_list)
random.shuffle(generated_text_list)
generated_text = ''.join(generated_text_list)
with open('case.txt', 'w') as file:
    file.write(generated_text)
