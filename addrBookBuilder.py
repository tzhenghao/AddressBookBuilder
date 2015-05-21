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

# CONSTANTS
NUMARGS = 2
OUTPUTFILE = 'contacts.txt'

# EFFECTS: Returns the phone numbers if present, None if phone number is absent.
def phoneNumberHandler(text):
	phoneReg = re.compile(r'''(
		(\d{3}|\(\d{3}\)?)
		(\s|-|\.)?
		(\d{3})
		(\s|-|\.)
		(\d{4})
		(\s*(ext|x|ext.)\s*(\d{2,5}))?
		)''', re.I)
	phoneNums = phoneReg.findall(text)
	return phoneNums


# EFFECTS: Returns the email addresses if present, None if absent.
def emailAddrHandler(text):
	emailReg = re.compile(r'''(
		[a-zA-Z0-9._%+-]+ # username 
		@
		[a-zA-Z0-9.-]+
		\.[a-zA-Z]{2,4}
		)''',re.I)
	emails = emailReg.findall(text)
	print(str(len(emails)))
	return emails


# REQUIRES: The data structures of the contacts to be populated.
# EFFECTS: Prints out the contacts that are detectable by the program.
def printContacts():
	print('calling printContacts...')


# REQUIRES: The data structures of the contacts to be populated.
# EFFECTS: Saves the contacts that are detectable by the program into a file.
def saveContacts(output, names, phoneNums, emailAddresses):

	openedFile = open(output, 'w')

	for name in names:
		openedFile.write(name)
	
	for number in phoneNums:
		openedFile.write(number)

	for emailAddr in emailAddresses:
		openedFile.write(emailAddr)

	openedFile.close()

# Helper function.
def phoneAndEmailHelper(sentence):
	phoneNumber = phoneNumberHandler(sentence)
	emailAddr = emailAddrHandler(sentence)
	name = 'nothing' # TODO

	if len(phoneNumber) != 0:
		print(phoneNumber)

	if len(emailAddr) != 0:
		print(emailAddr)

	# Handle output to contacts.txt
	saveContacts(OUTPUTFILE, name, phoneNumber, emailAddr)

readFromFile = False

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

	openedFile.close()
# Handle clipboard
else:
	clipboardContent = str(pyperclip.paste())
	phoneAndEmailHelper(clipboardContent)
