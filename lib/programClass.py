# define dataclass for program
from datetime import datetime as dt
from dataclasses import dataclass
from typing import List
from pathlib import Path
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
            json_file_path (str): _description_
        
        Returns:
            None    
        """
        with open(json_file_path) as f:
            program_map = json.load(f)
        
        for w, ps in program_map.items():
            for h, p in ps.items():
                program = Program(p['name'], p['category'], w, h)
                self.programs.append(program)
                
        
    def extract_programs_by_weekday(self, weekday: str):
        """
        Extract programs by weekday.
        
        Args:
            weekday (str): _description_
        
        Returns:
            List[Program]: _description_
        """
        return [ p for p in self.programs if p.weekday == weekday ]
    
    def extract_programs_by_start_time(self, start_time: str):
        """
        Extract programs by start_time.
        
        Args:
            start_time (str): _description_
        
        Returns:
            List[Program]: _description_
        """
        return [ p for p in self.programs if p.start_time == start_time ]
    
    def extract_programs_by_category(self, category: str):
        """
        Extract programs by category.
        
        Args:
            category (str): _description_
        
        Returns:
            List[Program]: _description_
        """
        return [ p for p in self.programs if p.category == category ]
    
    def extract_programs_by_name(self, name: str):
        """
        Extract programs by name.
        
        Args:
            name (str): _description_
        
        Returns:
            List[Program]: _description_
        """
        return [ p for p in self.programs if p.name == name ]
    
    def extract_program(self, weekday: str, start_time: str):
        """
        Extract program by weekday, start_time, and category.
        
        Args:
            weekday (str): _description_
            start_time (str): _description_
            category (str): _description_
        
        Returns:
            Program: _description_
        """
        return [ p for p in self.programs if p.weekday == weekday and p.start_time == start_time ][0]
    

@dataclass
class RawItem:
    filename: str
    
    def __post_init__(self):
        self.yymmdd = '20' + self.filename[2:8]
        self.date = dt.strptime(self.yymmdd, '%Y%m%d')
        self.yymm = self.yymmdd[:6]
        self.weekday = str(self.date.weekday())
        self.start_time = self.filename.split('-')[1].split('.')[0]
        
    def get_saveName(self, p: Program):
        return f"{p.category}/{p.name}/{self.yymm}/{p.name}{self.filename}"