"""
NON-PRODUCTION TEST CODE
file: batch-compact.py
description: Basic wrapper for RapidCompact's CLI to batch-compact multiple 3D files and prepare them for import into Unreal Engine. This module is the main script for the wrapper.
language: python3
author: Aidan Grant / kittencurtain
"""

"""Psuedo:
import mkdir command from os module
import subprocess for rpdx execution
"""


def askUserForFiles():
  """Pseudo:
  1. ask user for input
    1a. each input should be one file, or users can specify a folder to process every file in that folder
  2. validate the input, report error if invalid
  3. if valid, add to list then ask user for next file/folder
  4. if input is empty, finish and return list
  """
  pass


def runCLICompact(assetList)
  """Pseudo:
  1. for each item in the asset list,
    1a. create a subdirectory for its output
    1b. compact the asset & export it to the subdirectory
    1c. print debug information for success/failure
  """
  pass


def checkForMoreFiles()
  """Pseudo:
  1. check if the user would like to process more files
  2. if the input is not empty, check if it is valid (y/n)
  3. if valid, check if y and return true
  4. otherwise, return false
  """

def main():
  """Pseudo:
  1. run the CLI batch compact with the files provided by the user
  2. print a success/failure line for each file
  3. check to see if the user would like to process more files
  """
  runCLICompact(askUserForFiles())
  
  while checkForMoreFiles():
    runCLICompact(askUserForFiles())
  
  print("Goodnight")


# Execution Below -----------

if __name__ == '__main__':
  main()
