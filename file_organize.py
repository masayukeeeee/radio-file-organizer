import os, pathlib
import re
from datetime import datetime as dt
import json
from shutil import ExecError

root_dir = '/Users/sakaimasayuki/Dropbox/radio'

with open(root_dir + '/script/program.json') as f:
    program_map = json.load(f)

def is_unnamed_file(fn):
    prog = re.compile(r'^AM\d{6}-\d{4}.MP3$')
    result = prog.match(fn)
    return result

def extract_time_info(fn):
    yymmdd = '20' + fn[2:8]
    date = dt.strptime(yymmdd, '%Y%m%d')
    yymm = yymmdd[:6]
    weekday = str(date.weekday())
    onair_time = fn.split('-')[1].split('.')[0]    
    return {'date':date, 'weekday':weekday, 'onair_time':onair_time, 'yymm':yymm}

def check_category_folder_existence(root_dir, category):
    return os.path.isdir(root_dir + '/{cat}/'.format(cat=category))

def check_title_folder_exsistence(root_dir, category, name):
    return os.path.isdir(root_dir + '/{cat}/{name}'.format(cat=category, name=name))

def check_monthly_folder_existence(root_dir, category, name, yymm):
    return os.path.isdir(root_dir + '/{cat}/{name}/{yymm}'.format(cat=category, name=name, yymm=yymm))


for fn in os.listdir(root_dir + '/uncategorized/'):
    if is_unnamed_file(fn):
        time = extract_time_info(fn)
        try:
            program_info = program_map[time['weekday']][time['onair_time']]
            name = program_info['name']
            category = program_info['category']
            yymm = time['yymm']
            if not check_category_folder_existence(root_dir, category):
                os.makedirs(root_dir + '/{category}/'.format(category=category))
            if not check_title_folder_exsistence(root_dir, category, name):
                os.makedirs(root_dir + '/{category}/{name}'.format(category=category, name=name))
            if not check_monthly_folder_existence(root_dir, category, name, yymm):
                os.makedirs(root_dir + '/{category}/{name}/{yymm}'.format(category=category, name=name, yymm=yymm))
            new_fn = root_dir + '/{category}/{name}/{yymm}/'.format(category=category, name=name, yymm=yymm) + name + fn
            os.rename(root_dir + '/uncategorized/' + fn, new_fn)
            print(fn + ' has renamed by ' + new_fn)
        except Exception as e:
            print('a program is not exist for ' + fn)
            print(e)
                    
print('done!!')