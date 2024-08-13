# Critical Process Detector (CPD)

## Overview

CPD is a Python script that analyzes binary files to identify specific Windows API functions and libraries using the r2pipe library. This tool helps detect the presence of critical system functions and libraries that may indicate potential process manipulation or critical operations within a binary.

# Prerequisites

To use CPD, ensure you have the following installed:

  1. [Radare2](https://book.rada.re/intro/intro.html) - A powerful open-source reverse engineering framework.
  2. [r2pipe](https://book.rada.re/scripting/r2pipe.html) - A Python library for interacting with Radare2.

Install r2pipe using pip:

```sh
pip install r2pipe
```
## Usage

Run the CPD script with the path to the binary you want to analyze. The script will analyze the binary and print out relevant information about the presence of specific functions and libraries.
## Command

```sh

python CPD.py <path to binary>
```
## Example

```sh
python CPD.py /path/to/your/binary.exe
```
## Output

The script will produce output indicating whether the following components are found in the binary:

  `ntdll.dll`: Indicates that the ntdll.dll library is present.
  `NtSetInformationProcess`: A function often used in process manipulation.
  `RtlSetProcessIsCritical`: A function used to mark a process as critical, affecting system behavior.

## How It Works

1. Open Binary: The script opens the specified binary file using r2pipe and Radare2.
2. Analyze Imports: It performs a full analysis of symbols and imports using the command aaa;iij.
3. Detect Components: The script parses the results to check for the presence of ntdll.dll, NtSetInformationProcess, and RtlSetProcessIsCritical.
4. Print Results: It prints messages to the console if any of the specified components are found.
## Example Output

The script will produce output indicating whether the following components are found in the binary:
```css
[+] Found ntdll.dll
[+] Found NtSetInformationProcess
[+] Found RtlSetProcessIsCritical
```

# Important Note

  This is a POC & a fun project that helped me understand the r2pipe libray but this is by no way a effective way to detect those imports. Attackers can easily hide the imports from static analysis tools like this script, for example packing would be the easiest way to acheive that.
