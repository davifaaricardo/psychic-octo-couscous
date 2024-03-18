
import shutil
import os
def decompile(jar_file,extract_dir):
  filename = jar_file.replace('.jar','.zip')
  print('warning utilizing decompiler.decompile(x,y) if this is installed where the argument `jar_file` is not it will NOT work'.upper())
  os.rename(jar_file, filename)
  shutil.unpack_archive(filename, extract_dir)
