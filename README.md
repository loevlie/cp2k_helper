# cp2k_helper
This is a package I plan on building up throughout my Ph.D. to help accelerate my work with cp2k.

CP2K is a quantum chemistry and solid state physics software package.  I will explain some of the functionalities I have build so far below.

## output_parser

You can use this class to retreive information from the output files generated after running a calculation using cp2k.  The class will retrieve all information under the given directory (with a max depth as an optional extra argument) and use the directory names to classify each calculation you ran.  Therefore, you should not have two seperate cp2k calculations with the same directory name.  An example is shown below:

The output will be a dictionary of dictionaries (Containing the single point Energy calculations and Geometric optimization final energies found under the specified directory)

```python3
# Depth automatically set to inf
parser = output_parser(base_file_path='./cp2k') 
# If all=False then only the final energies will be retrieved
Energies = parser.get_energies(all=False) 
print(Energies)
```
**Output:**
```
{'ENERGY': defaultdict(float,
             {'Folder_Name1': -1000.997638482306,
              'Folder_Name2': -1000.997638482306,
              'Folder_Name8': -1000.900349392778,
              'Folder_Name6': -1000.900349392778}),
 'GEO_OPT': defaultdict(None,
             {'Folder_Name5': -1000.900349392778,
              'Folder_Name7': -1000.997638482306,
              'Folder_Name3': -1000.900349392778,
              'Folder_Name4': -1000.900349392778})}
```

The output example has fake foldernames and energy values for proprietary reasons.

## Contribute to cp2k helper

If you have any ideas of features that would be nice to have in cp2k helper please reach out to me or submit a pull request! 