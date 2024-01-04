"""
define dataclass for program
"""

from datetime import datetime as dt
from dataclasses import dataclass
import json

@dataclass
class Program:
    """
    This class is for managing program information.
    
    Attributes:
        name: name of program.
        category: category of program.
        weekday: weekday of program.
        start_time: start time of program.
        end_time: end time of program.
    """
    name: str
    category: str
    weekday: str
    start_time: str

class Schedule:
    """
    This class is for managing schedule of programs.
    
    Attributes:
        programs: List of Program objects.
    
    Methods:
        - load programs from json file.
        - extract programs by weekday / start_time / category.
    """

    def __init__(self):
        self.programs = []

    def load_programs(self, json_file_path: str):
        """
        Load program information from json file.
        
        Args:
            json_file_path (str): path to json file.
        
        Returns:
            None    
        """
        with open(json_file_path, 'r', encoding='utf-8') as f:
            program_map = json.load(f)

        for w, ps in program_map.items():
            for h, p in ps.items():
                program = Program(p['name'], p['category'], w, h)
                self.programs.append(program)


    def extract_programs_by_weekday(self, weekday: str):
        """
        Extract programs by weekday.
        
        Args:
            weekday (str): monday is 0, tuesday is 1, ...
        
        Returns:
            List[Program]: list of program instances.
        """
        return [ p for p in self.programs if p.weekday == weekday ]

    def extract_programs_by_start_time(self, start_time: str):
        """
        Extract programs by start_time.
        
        Args:
            start_time (str): hhmm. 0000 - 2359
        
        Returns:
            List[Program]: list of program instances.
        """
        return [ p for p in self.programs if p.start_time == start_time ]

    def extract_programs_by_category(self, category: str):
        """
        Extract programs by category.
        
        Args:
            category (str): english or comedian
        
        Returns:
            List[Program]: list of program instances.
        """
        return [ p for p in self.programs if p.category == category ]

    def extract_programs_by_name(self, name: str):
        """
        Extract programs by name.
        
        Args:
            name (str): title of program.
        
        Returns:
            List[Program]: list of program instances.
        """
        return [ p for p in self.programs if p.name == name ]

    def extract_program(self, weekday: str, start_time: str):
        """
        Extract program by weekday, start_time, and category.
        
        Args:
            weekday (str): monday is 0, tuesday is 1, ...
            start_time (str): hhmm. 0000 - 2359
            category (str): english or comedian
        
        Returns:
            Program: program instance.
        """
        res = [ p for p in self.programs if p.weekday == weekday and p.start_time == start_time ][0]
        return res


@dataclass
class RawItem:
    """
    This class is for managing raw item.
    """
    filename: str

    def __post_init__(self):
        self.yymmdd = '20' + self.filename[2:8]
        self.date = dt.strptime(self.yymmdd, '%Y%m%d')
        self.yymm = self.yymmdd[:6]
        self.weekday = str(self.date.weekday())
        self.start_time = self.filename.split('-')[1].split('.')[0]

    def get_save_name(self, p: Program):
        """
        Get save name of the file.
        """
        return f"{p.category}/{p.name}/{self.yymm}/{p.name}{self.filename}"
