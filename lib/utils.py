import os, pathlib
import re
from datetime import datetime as dt
import json
from shutil import ExecError

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
