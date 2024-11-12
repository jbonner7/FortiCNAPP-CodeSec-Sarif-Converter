# FortiCNAPP-CodeSec-Sarif-Converter
A simple python script to convert Lacework FortiCNAPP SARIF files to CSV

## Overview
FortiCNAPP SAST & SCA features with Code Security use SARIF as the default output format. This script uses Python's json and csv libraries to read the SARIF file (which is in JSON format) and output relevant data to CSV.

This example script extracts key information, such as rule ID, message, severity, and file location. You can customize the fields based on the specific data you need from the SARIF file.

## Explanation
* **Tool Name**, **Branch**, **Repository URI**, and **Commit ID**: These are extracted from the tool and versionControlProvenance sections.

* **Results**: If there are any issues, they are processed by extracting the ruleId, message, level (severity), file, and line information.

* **Empty Results**: If there are no results, only basic information (tool, branch, repository, and commit) is logged.

## How to Use the Script
Save the script as sarif_to_csv.py.
Run the script with Python:
```
python sarif_to_csv.py
```

This end result is a versatile CSV that includes project version control data, useful even when there are no results to report, which should make analysis easier in Excel.
