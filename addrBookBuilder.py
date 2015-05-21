# Name: Zheng Hao Tan
# Email: tanzhao@umich.edu
# Date: May 16, 2015

# This program will read in web pages and extract names and email addresses and
# and save them to a list of contacts.

# Usage
# TODO

import pyperclip # For clipboard usage.
import re # For regular expression usage.
import sys
import os # For file streams

# TODO - Handle names.

# EFFECTS: Returns the phone numbers if present, None if phone number is absent.
def phoneNumberHandler():
	phoneReg = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
	phoneNums = phoneNums.findall()

# EFFECTS: Returns the email addresses if present, None if absent.
def emailAddrHandler():
	emailReg = re.compile(r'@+(\.com | \.edu)')
	emails = emailReg.findall()

# REQUIRES: The data structures of the contacts to be populated.
# EFFECTS: Prints out the contacts that are detectable by the program.
#def printContacts():

# REQUIRES: The data structures of the contacts to be populated.
# EFFECTS: Saves the contacts that are detectable by the program into a file.
#def saveContacts():

readFromFile = False

if len(sys.argv) < 2:
	print('Reading from clipboard...')
elif len(sys.argv) == 2:
	print('Reading from ' + str(sys.argv[1]) + '...')
	readFromFile = True
else:
	print('Error: Too many arguments for this program!')
	sys.exit()

# Handle read from File
if readFromFile:
	openedFile = open(sys.argv[1])
	fileContent = openedFile.readlines()
else:
	clipboardContent = pyperclip.paste()
