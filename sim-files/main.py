
#       main.py
#       
#       Copyright 2010 Alex Dumitrache <alex@cimr.pub.ro>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from __future__ import division

try:
    from profilestats import profile
except:
    print "No profiling"
    pass
    
    


print "robot-sandbox (development version) starting..."
print " "

import cellulose    # nu-l gaseste py2exe
import cellulose.extra    # nu-l gaseste py2exe
import cellulose.extra.restrictions    # nu-l gaseste py2exe
import pprint

import sys
import os

try:
    import affinity
    affinity.set_process_affinity_mask(os.getpid(),1)
except:
    print "module affinity not found"

print "cwd: ", os.getcwd()
(path,file) = os.path.split(os.getcwd())

#print path
#print file

if file != 'sim-files':
    print "abs path: ", os.path.abspath(__file__)
    [basepath,file] = os.path.split(os.path.abspath(__file__))
    libpath = os.path.join(basepath, "dist", "library.zip")
    print "base folder:", basepath
    print "library zip:", libpath
    os.chdir(basepath)
    (path,file) = os.path.split(os.getcwd())
    if file == 'sim-files':
        pass
        #print "path is ok"
    else:
        print "WARNING: working folder is not 'sim-files'"
else:
    print "path is OK"    
    basepath = os.getcwd()

sys.basepath = basepath
#raise SystemExit




def rmrf(folder, exc = False):
    if sys.platform == "win32":
        rm = "rmdir /s /q"
    else:
        rm = "rm -rf"

    ret = os.system('%s "%s"' % (rm, folder))
    if exc:
        if ret != 0: 
            raise Exception, "error deleting " + folder

if os.path.isdir(os.path.join(basepath, "..", "upgradetmp")): 
    print "Deleting temporary files..."
    rmrf(os.path.normpath(os.path.join(basepath, "..", "upgradetmp")))


from vplus import *
import vplus



def which(program):
    import os
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

if sys.platform == 'win32':
    vplus._editor = os.path.join(basepath, "notepad2", "Notepad2.exe")
    if not os.path.exists(vplus._editor):
        vplus._editor = "notepad.exe"
    vplus._editor = '"' + vplus._editor + '"' 
else:
    editors = "gedit","kwrite", "vim", "vi"
    for e in editors:
        if which(e) != None:
            vplus._editor = which(e)
            break
    print "Editor is %s." % vplus._editor
    



# relpath for Py2.5
# source: http://mail.python.org/pipermail/python-list/2009-August/1215220.html
def relpath(path, start=os.path.curdir):
    """Return a relative version of a path"""

    if not path:
        raise ValueError("no path specified")
    start_list = os.path.abspath(start).split(os.path.sep)
    path_list = os.path.abspath(path).split(os.path.sep)
    if start_list[0].lower() != path_list[0].lower():
        return os.path.abspath(path)
    # Work out how much of the filepath is shared by start and path.
    for i in range(min(len(start_list), len(path_list))):
        if start_list[i].lower() != path_list[i].lower():
            break
    else:
        i += 1

    rel_list = [os.path.pardir] * (len(start_list)-i) + path_list[i:]
    if not rel_list:
        return os.path.curdir
    return os.path.join(*rel_list)
    

try:
    os.path.relpath
except:
    os.path.relpath = relpath

#ipshell = IPShellEmbed()
#ipshell() 

#~ @profile
def main():
    import viewer_gui


    sys.argv.append("--navigation-mode=Softimage")
    sys.argv.append("--verbose")
    sys.argv.append("scene.py")
    V = viewer_gui.Viewer()
    V.run()

main()

