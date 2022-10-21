"""
NowLoadY 2021.10
email:2225649558@qq.com
"""
import random
import time


def check_mode1_repeat():
    if check_repeat(Words_1) and check_repeat(Words_2) and check_repeat(Short_last_1) and check_repeat(Short_last_2):
        return 1
    else:
        return 0


def check_mode2_repeat():
    if check_repeat(Short_sentence_one) and check_repeat(Short_last_1) and check_repeat(Short_last_2):
        return 1
    else:
        return 0


def check_mode3_repeat():
    if check_repeat(Short_one_1) and check_repeat(Short_one_2) and check_repeat(Short_last_1) and check_repeat(Short_last_2):
        return 1
    else:
        return 0


def check_repeat(text):
    # print('start check')
    if used:
        for i, used_text in enumerate(used):
            # print(used_text)
            if text == used_text:
                # print('check_repeat repeat')
                return 0
                break
    # print('check_repeat ok')
    return 1


def random_choice(words_, short_sentence_one_, short_last_, short_one_):
    # print("random_choice")
    Words_1_ = random.choice(words_)
    Words_2_ = random.choice(words_)
    Short_sentence_one_ = random.choice(short_sentence_one_)
    Short_last_1_ = random.choice(short_last_)
    Short_last_2_ = random.choice(short_last_)
    Short_one_1_ = random.choice(short_one_)
    Short_one_2_ = random.choice(short_one_)
    return Words_1_, Words_2_, Short_sentence_one_, Short_last_1_, Short_last_2_, Short_one_1_, Short_one_2_
# 收集组句
short_sentence_one = []
for line in open("short_sentence_one.txt", encoding='utf-8'):
    line = line[:-1]
    short_sentence_one.append(line)
# 收集短散句
short_one = []
for line in open("short_one.txt", encoding='utf-8'):
    line = line[:-1]
    short_one.append(line)
# 收集结尾句
short_last = []
for line in open("short_last.txt", encoding='utf-8'):
    line = line[:-1]
    short_last.append(line)
# 收集词语
words = []
for line in open("words.txt", encoding='utf-8'):
    line = line[:-1]
    words.append(line)
# 收集诗句
# poetry = []
# for line in open("poetry.txt", encoding='utf-8'):
#    poetry.append(line)
# print(sentence_one[1])
# 按标点符号分割列表元素（每个句子）
# parts_one = []
# for sentence in sentence_one:
#    part = sentence.split("；")
#    # 得到sentence_one的拆分元素
#    parts_one.append(part)

# parts_two = []
# for sentence in sentence_two:
#    part = sentence.split("，")
#    # print(part)
#    # 得到sentence_one的拆分元素
#    parts_two.append(part)

# 展开嵌套列表
# parts_one = sum(parts_one, [])
# parts_two = sum(parts_two, [])

# 输出
print('how many sentences do you want to generate:')
times = input()
i = 0
used = []
time_start = time.time()
while i < int(times):
    output_mode = random.randint(1, 3)
    # print(output_mode)
    while output_mode == 1:
        Words_1, Words_2, Short_sentence_one, Short_last_1, Short_last_2, Short_one_1, Short_one_2 = random_choice(words, short_sentence_one, short_last, short_one)
        if Words_1 != Words_2 and Short_last_1 != Short_last_2 and check_mode1_repeat():
            output1 = (str(i + 1) + ': ' + Words_1 + '; ' + Words_2 + '; ' + Short_last_1 + '; ' + Short_last_2 + '!')
            print(output1)
            used.append(Words_1)
            used.append(Words_2)
            used.append(Short_last_1)
            used.append(Short_last_2)
            break
        else:
            continue
    while output_mode == 2:
        Words_1, Words_2, Short_sentence_one, Short_last_1, Short_last_2, Short_one_1, Short_one_2 = random_choice(words, short_sentence_one, short_last, short_one)
        if Short_last_1 != Short_last_2 and check_mode2_repeat():
            output2 = (str(i + 1) + ': ' + Short_sentence_one + '; ' + Short_last_1 + '; ' + Short_last_2 + '!')
            print(output2)
            used.append(Short_sentence_one)
            used.append(Short_last_1)
            used.append(Short_last_2)
            break
        else:
            continue

    while output_mode == 3:
        Words_1, Words_2, Short_sentence_one, Short_last_1, Short_last_2, Short_one_1, Short_one_2 = random_choice(words, short_sentence_one, short_last, short_one)
        if Short_one_1 != Short_one_2 and Short_last_1 != Short_last_2 and check_mode3_repeat():
            output3 = (
                    str(i + 1) + ': ' + Short_one_1 + '; ' + Short_one_2 + '; ' + Short_last_1 + '; ' + Short_last_2 + '!')
            print(output3)
            used.append(Short_one_1)
            used.append(Short_one_2)
            used.append(Short_last_1)
            used.append(Short_last_2)
            break
        else:
            continue
    i += 1
    if time.time()-time_start > 2:
        input('Press Enter to exit…')
input('Press Enter to exit…')
