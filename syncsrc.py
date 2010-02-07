#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-

from os import *
import sys


csfiletypes = ['*.c',
               '*.cpp',
               '*.java',
               '*.aidl'
              ]

if __name__ == '__main__':
    print """
    **** Starting Sync With repo_asus sync ****
    """

    for x in xrange(3):
        system('repo_asus sync')

    if len(sys.argv) == 2 and sys.argv[1] == 'cs':
        print """
        **** Starting Cscope Tagging ****
        """
        if len(csfiletypes) > 0:
            print ' --> using customized file types.'
            findcmd = 'find . -name "' + csfiletypes[0] + '"'
            for filetype in csfiletypes[1:]:
                findcmd = findcmd + ' -o -name "' + filetype + '"'
            system(findcmd + ' > cscope.files')
        else:
            print ' --> using cscope default file types.'
        print ' --> starting tagging...'
        system("cscope -qRUb > /dev/null")

    print """
    **** End of sync. ****
    """
