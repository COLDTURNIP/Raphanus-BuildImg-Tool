#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-

from os import *
from shutil import *
import sys

makefilename = 'buildspec.mk'
makefileSrc = 'vendor/asus/a10/'

imgFiles = ['userdata.img',
            'system_ext3_part1.img',
            'system_ext3_part2.img']
makeOutcomePath = 'out/target/product/a50/'
targetPath = 'build_img_output/'
    
if __name__ == '__main__':
    print """
    **** Raphanus's Image Building Process ****
    """
    
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == '-log'):
        if path.exists(makefilename):
            print '    --> replacing old makefile: ' + makefilename
            remove(makefilename)
        else:
            print '    --> copying makefile: ' + makefilename
        copy(makefileSrc + makefilename, '.')
        
        print '    --> start building'
        if len(sys.argv) == 2 and sys.argv[1] == '-log':
            system('make > cdipMakeLog.txt')
        else:
            system('make')
        print '    --> complete building process'

    filesToBeClean = set(listdir(targetPath)) & set(imgFiles)
    if filesToBeClean:
        print '    --> clearing output folder'
        for fileToBeClean in filesToBeClean:
            remove(targetPath + fileToBeClean)
    print '    --> copying output images to ' + targetPath
    for newFile in imgFiles:
        print '        * ' + newFile
        copy(makeOutcomePath + newFile, targetPath)

    print """
    You've got burning.
    """


