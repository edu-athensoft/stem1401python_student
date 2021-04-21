"""
part 2
question 1
"""

"""
function:       copy codes missing          5/10
structure:      failed to use function      1.0/2.5
convention:     ok                           2.5/2.5
comment:        ok                          0/2.5
user-friendly:  failed to use exception     1.5/2.5
                title or message missing

subtotal:       10.0
"""

from datetime import date
import os

os.mkdir('work')
os.mkdir('work{}src'.format(os.sep))
os.mkdir('work{}dest'.format(os.sep))

num_files_to_create = int(input('please enter the number of files you want to create:'))
for i in range(num_files_to_create):
    file_name = input('please enter the name of the files you want to create:')
    open(r'C:/Users/sdan7/stem1401python/py201220/work/src/{}.txt'.format(file_name), 'x')
today = date.today()
today_strftime = today.strftime('%Y-%m-%d')
for i in os.listdir(r'C:/Users/sdan7/stem1401python/py201220/work/src'):
    new_name = i + '_' + today_strftime
    open(r'C:/Users/sdan7/stem1401python/py201220/work/dest/{}.txt'.format(new_name), 'x')
