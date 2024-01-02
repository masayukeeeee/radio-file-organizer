import os
import re
from datetime import datetime as dt
from lib.programClass import Program, Schedule

def is_unnamed_file(fn: str):
    """
    Check if the file is unnamed file.
    
    Args:
        fn (str): file name

    Returns:
        bool: True if the file is unnamed file
    """
    prog = re.compile(r'^AM\d{6}-\d{4}.MP3$')
    result = prog.match(fn)
    return result

def extract_time_info(fn: str):
    """
    Extract time information from filename.

    Args:
        fn (str): file name

    Returns:
        Dict[str, str, str, str]: time information.
        date / weekday / onair_time / yymm
    """
    yymmdd = '20' + fn[2:8]
    date = dt.strptime(yymmdd, '%Y%m%d')
    yymm = yymmdd[:6]
    weekday = str(date.weekday())
    onair_time = fn.split('-')[1].split('.')[0]    
    return {'date':date, 'weekday':weekday, 'onair_time':onair_time, 'yymm':yymm}

def check_category_folder_existence(root_dir: str, 
                                    category: str):
    """
    Check if the category folder exists.
    
    Args:
        root_dir (str): root directory
        category (str): category name
        
    Returns:
        bool: True if the category folder exists
    """
    return os.path.isdir(root_dir + '/{cat}/'.format(cat=category))

def check_title_folder_exsistence(root_dir: str, 
                                  category: str,
                                  name: str):
    """
    Check if the title folder exists.
    
    Args:
        root_dir (str): root directory
        category (str): category name
        name (str): title name
        
    Returns:
        bool: True if the title folder exists
    """
    return os.path.isdir(root_dir + '/{cat}/{name}'.format(cat=category, name=name))

def check_monthly_folder_existence(root_dir: str,
                                   category: str,
                                   name: str,
                                   yymm: str):
    """
    Check if the monthly folder exists.
    
    Args:
        root_dir (str): root directory
        category (str): category name
        name (str): title name
        yymm (str): year and month
        
    Returns:
        bool: True if the monthly folder exists
    """
    return os.path.isdir(root_dir + '/{cat}/{name}/{yymm}'.format(cat=category, name=name, yymm=yymm))
    