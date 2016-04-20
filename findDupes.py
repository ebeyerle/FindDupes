import os, sys
import includes.stack

class FindDupes(object):
  def __init__(self):
    self.files = []
    self.dirs = []
    self.dupes = []
    self.stk = includes.stack.stack()

  def walk(self, folder):
    self.stk.push(folder)
    while not self.stk.empty():
      path = self.stk.top() 
      self.stk.pop()
      files = os.listdir(path)
      for x in files:
        fullpath = os.path.join(path, x)
        if os.path.isdir(fullpath):
          self.dirs.append(x)
          self.stk.push(fullpath)
        else:
          self.files.append(x)

  def findDupes(self):
    s = set(self.files)
    for x in self.files:
      if x in s:
        s.remove(x)
      else:
        self.dupes.append(x) 

  def display(self):
    print "The", len(self.files), "files are:"
    print self.files
    print("The following file(s) are duplicates")
    print self.dupes
    print("Directory list")
    print self.dirs


if __name__ == "__main__":
  if len(sys.argv) > 1:
    folder = sys.argv[1:]
    for i in folder:
      if os.path.exists(i):
        finder = FindDupes()
        finder.walk(i)
        finder.findDupes()
        finder.display()
      else:
        print("%s is not a valid folder" % i)
        sys.exit()
  else:
    print("No folder was typed in the command line")    

