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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
if __name__ == '__main__':
    '''
        Run Part
    '''

    latest = len(calls) - 1

    # Output
    print('First record of texts, %s texts %s at time %s' % \
            (texts[0][0], texts[0][1], texts[0][2]))
    print('Last record of calls, %s calls %s at time %s, lasting %s seconds' % \
            (calls[latest][0], calls[latest][1], calls[latest][2], calls[latest][3]))
