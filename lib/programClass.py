# define dataclass for program

from dataclasses import dataclass
from typing import List
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
    end_time: str

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
        
        