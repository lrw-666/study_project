import tkinter as tk
import re

# print(dir(tk))
# print(help(tk))
path = "{E:/Users/86153/Pictures/Camera Roll/001.png}"
end = '(gif|jpeg|jpg|png|pdf)'
regex = '[C-F]:/(\w+\s*\w+/)+\w+\s*\w+\.'+end
m = re.search(regex, path)
print(m)
if m:
    print(m.group())