# cp2k_helper
This is a package I plan on building up throughout my Ph.D. to help accelerate my work with cp2k.

CP2K is a quantum chemistry and solid state physics software package.  I will explain some of the functionalities I have built so far below.

# Installation 

Please run the following in your terminal where you would like to install the package directory.
```
git clone https://github.com/loevlie/cp2k_helper.git
pip install -e cp2k_helper
```

I am pretty sure you can update cp2k_helper later by just going to the directory and running:

```
git pull
```

# Example Usage

## output_parser
**Uses**

* Retreive information from the output files generated after running a calculation using cp2k. 

**Important Note** 

* The class will retrieve all information under the given directory (with a max depth as an optional extra argument) and use the directory names to classify each calculation you ran.  Therefore, you should not have two seperate cp2k calculations with the same directory name.  


**Example**

The output will be a dictionary of dictionaries (Containing the single point Energy calculations and Geometric optimization final energies found under the specified directory)

```python3
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

cp2k_helper can quickly get you the final energy values from all GEO_OPT or ENERGY DFT calculations under a specified directory.  They are saved as a csv (optionally you may name it whatever you want but the default is Energies.csv).  An example of using this feature for all of the calculations under the current folder is below:

```
cp2k_helper --energy . My_Energy_Values
```

The above command will save a csv file to your current directory with all of the energy values along with the type of calculation run and the folder name of each.  

**TODO:**
Add optional information to the csv file on the following
1. Functional
2. Convergence criteria
3. Atomic composition
4. Etc. (if anyone has other information they think would be useful please add it to this list)

# Contribute to cp2k helper

If you have any ideas for features that would be nice to have in cp2k_helper please reach out to me or submit a pull request! 

# Reporting Issues

Please report issues at https://github.com/loevlie/cp2k_helper/issues.

