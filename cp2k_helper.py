import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO   # StringIO behaves like a file object
import os
from collections import defaultdict

# HELPER FUNCTIONS

def search_util(root='.',depth=np.inf,parse_by = None):
    """  Recursively find all files in a directory.
    root - This is the directory you would like to find the files in, defaults to cwd
    Args:
        root (str, optional): The directory you would like to recursively search through. Defaults to '.'.
        parse_by (str, optional): If string is provided the output files will contain the string in the path
    Returns:
        list: All files under the directory specified
    """
    files = []
    root = os.path.abspath(os.path.expanduser(os.path.expandvars(root)))
    if parse_by: 
        for r, d, f in os.walk(root):
            if r[len(root):].count(os.sep) < depth:
                for file in f:
                    if parse_by in file:
                        files += [os.path.join(r, file)]
    else:
        for r, d, f in os.walk(root):
            if r[len(root):].count(os.sep) < depth:
                for file in f:
                    files += [os.path.join(r, file)]
    return files

def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

class output_parser:
    def __init__(self,base_file_path='.',depth=np.inf):
        self.base_file_path=base_file_path
        # We should add init statements to find a list of all of the important files
        self.opt_files = search_util(base_file_path,parse_by='OPT.out',depth=depth)
        parent_dirs = []
        for file in self.opt_files:
            parent_dir = os.path.split(os.path.split(os.path.realpath(file))[0])[1]
            parent_dirs.append(parent_dir)
        assert not checkIfDuplicates(parent_dirs), "There are duplicate directory names in your given base path"
        self.parent_dirs = parent_dirs
        self.input_files = search_util(base_file_path,parse_by='.inp',depth=depth)
        self.run_types = defaultdict(str)
        self.all_energies = {'ENERGY':defaultdict(float),'GEO_OPT':defaultdict()}


    def get_run_types(self):
        for file in self.input_files:
            inp_file = file
            with open(inp_file,'r') as g:
                inp_file1 = g.read()
            inp = np.genfromtxt(StringIO(inp_file1),delimiter='\t',dtype='str',skip_header=1)
            line = np.flatnonzero(np.char.find(inp,'RUN_TYPE')!=-1)
            assert len(line) == 1 # There seems to be more than one line in the input file for "RUN_TYPE"
            parent_dir = os.path.split(os.path.split(os.path.realpath(file))[0])[1]
            self.run_types[parent_dir] = inp[line][0].strip().split()[-1]

        return self.run_types


    def get_energies(self,all=True):
        """This function parses the OPT.out files under the given directory and outputs the energy values

        Args:
            all (bool, optional): If True - Output all energy values| If False - Output final energy value. Defaults to True.
        Returns:
            dict: A dictionary of lists with the energy values from each directory 
        """
        # TODO add functionality to choose between getting single point and GEO_OPT energies
        run_types = self.get_run_types()
        if all:
            for file in self.opt_files:
                Out_File = file
                with open(Out_File,'r') as g:
                    Out_File1 = g.read()
                out = np.genfromtxt(StringIO(Out_File1),delimiter='\t',dtype='str',skip_header=1)
                lines = np.flatnonzero(np.char.find(out,'ENERGY| Total FORCE_EVAL ( QS ) energy (a.u.):')!=-1)
                parent_dir = os.path.split(os.path.split(os.path.realpath(file))[0])[1]
                if run_types[parent_dir]=='GEO_OPT':
                    self.all_energies['GEO_OPT'][parent_dir] = []
                for line in lines:
                    if run_types[parent_dir]=='ENERGY':
                        self.all_energies[run_types[parent_dir]][parent_dir] = float(out[line].split()[-1])
                    elif run_types[parent_dir]=='GEO_OPT':
                        self.all_energies[run_types[parent_dir]][parent_dir].append(float(out[line].split()[-1]))
            Energy = self.all_energies
        else:
            for file in self.opt_files:
                Out_File = file
                with open(Out_File,'r') as g:
                    Out_File1 = g.read()
                out = np.genfromtxt(StringIO(Out_File1),delimiter='\t',dtype='str',skip_header=1)
                lines = np.flatnonzero(np.char.find(out,'ENERGY| Total FORCE_EVAL ( QS ) energy (a.u.):')!=-1)
                parent_dir = os.path.split(os.path.split(os.path.realpath(file))[0])[1]
                self.all_energies[run_types[parent_dir]][parent_dir] = float(out[lines[-1]].split()[-1])
            Energy = self.all_energies

        return Energy