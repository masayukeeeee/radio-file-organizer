import os
from pathlib import Path
import re
from datetime import datetime as dt
import json
from shutil import ExecError

from lib.utils import is_unnamed_file, extract_time_info, check_category_folder_existence, check_title_folder_exsistence, check_monthly_folder_existence

ROOT_DIR = Path(__file__).resolve().parents[1]
SCR_DIR = ROOT_DIR / 'script'

with open(SCR_DIR / 'program.json') as f:
    program_map = json.load(f)


# for fn in os.listdir(root_dir + '/uncategorized/'):
#     if is_unnamed_file(fn):
#         time = extract_time_info(fn)
#         try:
#             program_info = program_map[time['weekday']][time['onair_time']]
#             name = program_info['name']
#             category = program_info['category']
#             yymm = time['yymm']
#             if not check_category_folder_existence(root_dir, category):
#                 os.makedirs(root_dir + '/{category}/'.format(category=category))
#             if not check_title_folder_exsistence(root_dir, category, name):
#                 os.makedirs(root_dir + '/{category}/{name}'.format(category=category, name=name))
#             if not check_monthly_folder_existence(root_dir, category, name, yymm):
#                 os.makedirs(root_dir + '/{category}/{name}/{yymm}'.format(category=category, name=name, yymm=yymm))
#             new_fn = root_dir + '/{category}/{name}/{yymm}/'.format(category=category, name=name, yymm=yymm) + name + fn
#             os.rename(root_dir + '/uncategorized/' + fn, new_fn)
#             print(fn + ' has renamed by ' + new_fn)
#         except Exception as e:
#             print('a program is not exist for ' + fn)
#             print(e)
                    
# print('done!!')