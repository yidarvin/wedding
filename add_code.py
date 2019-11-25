
import argparse
import glob
import os
from os import listdir,mkdir,rmdir
from os.path import join,isdir,isfile,split
import sys

import cv2
import numpy as np

def add_qr_code_single_file(path_std, path_qr, path_save):
  std = cv2.imread(path_std)
  qr  = (cv2.imread(path_qr)[:,:,0] == 0) + 0
  text = (cv2.imread('/Users/darvin/origami/TEXT.png')[:,:,0] > 100) + 0
  
  # setting up std so that it is between 1 and 255 and all even
  std = np.clip(std, 1,255)
  for ii in range(3):
    std[:,:,ii] -= (std[:,:,ii] % 2)
  
  qr_pad = np.pad(qr, ((0,std.shape[0]-qr.shape[0]), (0,std.shape[1]-qr.shape[1])),
                  mode='constant', constant_values=0)
  text_pad = np.pad(text, ((std.shape[0]-text.shape[0],0), (std.shape[1]-text.shape[1],0)),
  mode='constant', constant_values=0)
  for ii in range(3):
    std[:,:,ii] += qr_pad.astype(np.uint8)
    std[:,:,ii] += text_pad.astype(np.uint8)
  
  cv2.imwrite(path_save, std)

def add_qr_code_batch(path_stds, path_qrs, path_save):
  for ii,path_img in enumerate(glob.glob(join(path_stds, '*.png'))):
    _, name_img = split(path_img)
    add_qr_code_single_file(path_img, join(path_qrs,name_img), join(path_save,name_img))

def main(args):
  parser = argparse.ArgumentParser(description = 'add_code')
  parser.add_argument('--std', dest='path_std', type=str, default=None)
  parser.add_argument('--qr', dest='path_qr', type=str, default=None)
  parser.add_argument('--save', dest='path_save', type=str, default=None)
  opts = parser.parse_args(args[1:])
  
  if isfile(opts.path_std) and isfile(opts.path_qr):
    add_qr_code_single_file(opts.path_std, opts.path_qr, opts.path_save)
  elif isdir(opts.path_std) and isdir(opts.path_qr) and isdir(opts.path_save):
    add_qr_code_batch(opts.path_std, opts.path_qr, opts.path_save)
  else:
    print('Something went wrong.')

if __name__ == '__main__':
  main(sys.argv)
