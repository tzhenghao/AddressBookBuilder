# Name: Zheng Hao Tan
# Email: tanzhao@umich.edu
# Date: May 16, 2015

# This program will read in web pages and extract names and email addresses and
# and save them to a list of contacts.

# USAGE: python3 addrBookBuilder.py <input file (optional)>')

import pyperclip # For clipboard usage.
import re # For regular expression usage.
import sys
import os # For file streams

# TODO - Handle names.
#def nameHandler(text):

# EFFECTS: Returns the phone numbers if present, None if phone number is absent.
def phoneNumberHandler(text):
	phoneReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	phoneNums = phoneReg.findall(text)
	return phoneNums


# EFFECTS: Returns the email addresses if present, None if absent.
def emailAddrHandler(text):
	print('hehehoidnjwaonidwa')
	emailReg = re.compile(r'@+(\.com|\.edu)')
	emails = emailReg.findall(text)
	return emails


# REQUIRES: The data structures of the contacts to be populated.
# EFFECTS: Prints out the contacts that are detectable by the program.
def printContacts():
	print('calling printContacts...')

# REQUIRES: The data structures of the contacts to be populated.
# EFFECTS: Saves the contacts that are detectable by the program into a file.
def saveContacts(output):
	openedFile = open(output, 'w')
	openedFile.write('lala')

# Helper function.
def phoneAndEmailHelper(sentence):
	phoneNumber = phoneNumberHandler(sentence)
	emailAddr = emailAddrHandler(sentence)

	if len(phoneNumber) != 0:
		print(phoneNumber)

	if len(emailAddr) != 0:
		print(emailAddr)

	# Handle output to contacts.txt
	saveContacts(OUTPUTFILE)

readFromFile = False
NUMARGS = 2
OUTPUTFILE = 'contacts.txt'

# Handle command line arguments
if len(sys.argv) < NUMARGS:
	print('Reading from clipboard...')
elif len(sys.argv) == NUMARGS:
	print('Reading from ' + str(sys.argv[1]) + '...')
	readFromFile = True
else:
	print('Error: Too many arguments for this program!')
	print('USAGE: python3 addrBookBuilder.py <input file (optional)>')
	sys.exit()

# Handle read from file
if readFromFile:
	openedFile = open(sys.argv[1])
	fileContent = openedFile.readlines()

	for sentence in fileContent:
		phoneAndEmailHelper(sentence)

# Handle clipboard
else:
	clipboardContent = pyperclip.paste()
	phoneAndEmailHelper(clipboardContent)

