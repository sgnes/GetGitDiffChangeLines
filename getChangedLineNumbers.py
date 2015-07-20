#! C:\python27\python
# coding = utf-8
__author__ = 'DZMP8F'


import os
import sys
import re

def get_detail_change_lines(diff):
    re_start_line = re.compile("(@@ -\d+,\d+ +\+)(\d+)(,\d+ @@)")
    start_line = 0
    change_lines = []
    chang_dict = {}
    for line in diff:
        #print line
        if line.startswith("@@"):
            re_start_line_g = re_start_line.match(line)
            if re_start_line_g:
                start_line = int(re_start_line_g.group(2))-1
                #print start_line
            else:
                pass
                #print line
        elif line.startswith("+") and start_line > 0:
            start_line = start_line + 1
            change_lines.append(start_line)
        elif line.startswith("-"):
            pass
        elif start_line > 0:
            start_line = start_line + 1
        else:
            pass
   # print change_lines
    return change_lines


    pass
def get_file_name(line):
    com = re.compile(r"(diff --git a)(.*)( b/)")
    m = com.match(line)
    file_name = ""
    if m:
        file_name = m.group(2)
    return file_name


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = raw_input("input file name:")
commsg_file = open(sys.argv[1])
if commsg_file:
    line = commsg_file.readline()
    res_dict = {}
    while line:
        if line.startswith("diff --git"):
            file_name = get_file_name(line)
            #print file_name
            detail_change = []
            while line:
                line = commsg_file.readline()
                if(line.startswith("diff --git")):
                    res_dict[file_name] = get_detail_change_lines(detail_change)
                    break
                detail_change.append(line)
            if not line:
                res_dict[file_name] = get_detail_change_lines(detail_change)
        else:
            line = commsg_file.readline()
    print res_dict

