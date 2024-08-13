###
# pip install r2pipe
###
# Usage: python CPD.py <path to binary>

import r2pipe
import sys
import json

## library flags
ndtdllFlag= 0

r2 = r2pipe.open(sys.argv[1])

imports = r2.cmd('aaa;iij')  # analyze all symbols and imports:
imports = json.loads(imports)

for ii in imports:
        
    if ii['libname'] == 'ntdll.dll' and ndtdllFlag < 1 :
            ndtdllFlag = ndtdllFlag + 1
            print("[+] Found ntdll.dll")
            
    if ii['name'] == 'NtSetInformationProcess':
        print("[+] Found NtSetInformationProcess")
        
    if ii['name'] == 'RtlSetProcessIsCritical':
        print("[+] Found RtlSetProcessIsCritical")


r2.quit()
sys.exit(0)
    
