# [![PyPi Version](https://img.shields.io/pypi/v/cp2k-helper.svg)](https://pypi.org/project/cp2k-helper/0.0.2/)

<h1 align="center">cp2k_helper</h1>

This is a package I plan on building up to help accelerate working with cp2k.

CP2K is a quantum chemistry and solid state physics software package.  I will explain some of the functionalities I have built so far below.

# Installation 
Installation through PyPi:
```
pip install cp2k_helper
```

Install through GitHub:


Run the following in your terminal where you would like to install the package directory.
```
git clone https://github.com/loevlie/cp2k_helper.git
pip install -e cp2k_helper
```

# Example Usage

## output_parser
**Uses**

* Retreive information from the output files generated after running a calculation using cp2k. 

**Important Note** 

* The class will retrieve all information under the given directory (with a max depth as an optional extra argument) and use the directory names to classify each calculation you ran.  Therefore, you should not have two seperate cp2k calculations with the same directory name.  


**Example**

The output will be a dictionary of dictionaries (containing the single point energy calculations and geometric optimization final energies found under the specified directory)

```python3
from cp2k_helper import output_parser
# Depth automatically set to inf
parser = output_parser(base_file_path='./cp2k') 
# If all=False then only the final energies will be retrieved
Energies = parser.get_energies(all=False) 
print(Energies)
```
**Output:**
```python3
{'ENERGY': defaultdict(float,
             {'Folder_Name1': -1000.997638482306,
              'Folder_Name2': -1000.997638482306,
              'Folder_Name6': -1000.900349392778}),
 'GEO_OPT': defaultdict(None,
             {'Folder_Name5': -1000.900349392778,
              'Folder_Name7': -1000.997638482306,
              'Folder_Name3': -1000.900349392778,
              'Folder_Name4': -1000.900349392778})}
```


**Note:** 

The output example has fake foldernames and energy values for proprietary reasons.

## Command Line tools

### **restart**

cp2k_helper has a handy command line tool for restarting a calculation if it timed out.  Just execute the command below in the directory that the calculation timed out and a new subdirectory will be created for the new job.  You can then submit the new job to restart the calculation.  

```
cp2k_helper --restart 
```

### **summ**

cp2k_helper can give you a quick summary of your output file.  Just use the command below with your output filename:

```
cp2k_helper --summ OPT.out
```

### **energy**

cp2k_helper can quickly get you the final energy values from all GEO_OPT or ENERGY DFT calculations under a specified directory.  The values are converted from Ha to eV.  They are saved as a csv (optionally you may name it whatever you want but the default is Energies.csv).  An example of using this feature for all of the calculations under the current folder is below:

```
cp2k_helper --energy . My_Energy_Values
```

The above command will save a csv file to your current directory with all of the final energy values along with the type of calculation run and the folder name of each.  As of now the .csv file will look similar to below (if you had 4 DFT calculations in the given directory).

**Energies.csv**

<div align="center">
  
| Folder_Name   | Type          | Energy (eV)   |
| ------------- | ------------- | ------------- |
| Folder_1      | GEO_OPT       | -10000.34324  |
| Folder_2      | ENERGY        | -10000.34324  |
| Folder_3      | ENERGY        | -10100.34324  |
| Folder_4      | GEO_OPT       | -10000.34324  |
  
</div>

**TODO:**
Add optional information to the csv file on the following
- [ ] Functional
- [ ] Did the calculation converge? (this one is important/useful)
- [ ] Convergence criteria
- [ ] Atomic composition
- [ ] Etc. (if anyone has other information they think would be useful please add it to this list)

# Contribute to cp2k helper

If you have any ideas for features that would be nice to have in cp2k_helper please reach out to me or submit a pull request! 

# Reporting Issues

Please report issues at https://github.com/loevlie/cp2k_helper/issues.

