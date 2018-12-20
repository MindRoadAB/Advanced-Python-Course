#!"C:\Users\Antoine Homsi\Desktop\Avancerad pythonprogrammering_Kurse\tryClick\env_Click\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'myClick==0.1','console_scripts','myClick'
__requires__ = 'myClick==0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('myClick==0.1', 'console_scripts', 'myClick')()
    )
