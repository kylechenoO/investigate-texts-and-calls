"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
'There are <count> different telephone numbers in the records.'"""

if __name__ == '__main__':
    '''
        Run Part
    '''

    ltexts = len(texts)
    lcalls = len(calls)
    result = set()

    i = 0
    while i < ltexts:
        result.add(texts[i][0])
        result.add(texts[i][1])
        i += 1

    i = 0
    while i < lcalls:
        result.add(calls[i][0])
        result.add(calls[i][1])
        i += 1

    #Output
    print('There are %d different telephone numbers in the records.' % (len(result)))
