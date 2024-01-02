import os
from pathlib import Path

from lib.utils import is_unnamed_file
from lib.programClass import Program, Schedule, RawItem

ROOT_DIR = Path(__file__).resolve().parents[1]
SCR_DIR = ROOT_DIR / 'script'
TMP_DIR = ROOT_DIR / 'uncategorized'

s = Schedule()
s.load_programs(SCR_DIR / 'program.json')

unnamed_mp3_files = [RawItem(f.name) for f in TMP_DIR.iterdir() if f.is_file() and is_unnamed_file(f.name)]

for raw_item in unnamed_mp3_files:
    try:
        p = s.extract_program(raw_item.weekday, raw_item.start_time)
        new_fn = raw_item.get_saveName(p)

        # make directory
        if not os.path.isdir(ROOT_DIR / p.category):
            os.makedirs(ROOT_DIR / p.category)
        if not os.path.isdir(ROOT_DIR / p.category / p.name):
            os.makedirs(ROOT_DIR / p.category / p.name)
        if not os.path.isdir(ROOT_DIR / p.category / p.name / raw_item.yymm):
            os.makedirs(ROOT_DIR / p.category / p.name / raw_item.yymm)
        
        os.rename(TMP_DIR / raw_item.filename, ROOT_DIR / new_fn)
        print(f'{raw_item.filename} has renamed by {new_fn}')
    except Exception as e:
        print(f'a program is not exist for {raw_item.filename}')
        print(e)

# import ipdb; ipdb.set_trace()

print('done!!')