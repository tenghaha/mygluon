#!D:\Anaconda3\envs\gluon\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'notedown==1.5.0','console_scripts','notedown'
__requires__ = 'notedown==1.5.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('notedown==1.5.0', 'console_scripts', 'notedown')()
    )
