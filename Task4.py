"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

def getSalesPhone(calllist, textlist):
    '''
        Get all sales number
    '''

    call_out_list = []
    except_list = []
    result_list = []
    for callline in calllist:
        call_out_list.append(callline[0])
        except_list.append(callline[1])

    for textline in textlist:
        except_list.append(textline[0])
        except_list.append(textline[1])

    for call_num in call_out_list:
        if call_num not in except_list:
            result_list.append(call_num)

    return result_list

if __name__ == '__main__':
    '''
        Run Part
    '''

    result_list = list(set(getSalesPhone(calls, texts)))
    result_list.sort()
    print('These numbers could be telemarketers:')
    for result in result_list:
        print(result)
