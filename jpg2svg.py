
import argparse
import os
from os import listdir,mkdir,rmdir
from os.path import join,isdir,isfile,split
import sys

import cv2
import numpy as np

def convert_single_file(path_file, path_temp):
  path_src,name_root = split(path_file)
  name_root = name_root[:-4]
  
  # Reading in the image.
  name_invt = name_root + '.png'
  img = cv2.imread(path_file)
  img_resize = cv2.resize(img, (1024,1024), interpolation=cv2.INTER_CUBIC)
  img_invert = 255 - img_resize
  if path_temp:
    cv2.imwrite(join(path_temp, name_invt), img_invert)
  else:
    cv2.imwrite(join(path_src, name_invt), img_invert)
  
  # Running conversion scripts.
  #name_temp = name_root + '.ppm'
  #name_save  = name_root + '.svg'
  #os.system("convert %s %s"%(name_invt, name_temp))
  #os.system("potrace -s %s -o %s"%(name_temp, name_save))

def main(args):
  parser = argparse.ArgumentParser(description = 'jpg2svg')
  parser.add_argument('--file', dest='path_file', type=str, default=None)
  parser.add_argument('--dir', dest='path_dir', type=str, default=None)
  parser.add_argument('--temp', dest='path_temp', type=str, default=None)
  opts = parser.parse_args(args[1:])
  
  if opts.path_file:
    convert_single_file(opts.path_file, opts.path_temp)
  
if __name__ == '__main__':
  main(sys.argv)
