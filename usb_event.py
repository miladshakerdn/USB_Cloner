import os
import re

def list_last_drives():
    '''
    Return all logical driver (for windows)
    '''
    regex = r"([^\s]*:)"
    driver = os.popen("wmic logicaldisk get name").read()

    return re.findall(regex, driver)