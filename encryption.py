from re import A
from cryptography.fernet import Fernet

# importing Flask and other modules
from flask import Flask, request, redirect, render_template, flash
import random
from random import randint

# import AES
from Crypto.Cipher import AES
from secrets import token_bytes

from flask.sessions import NullSession

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes

# 128 bits
key = token_bytes(16)

# Flask constructor
app = Flask(__name__, static_folder="static")

# A home route
@app.route('/')
@app.route('/home')
def home():
	return render_template("index.html")

# A decorator used to tell the application
# which URL is associated function
@app.route('/encryption', methods =["GET", "POST"])
def encryption():
	message = ''
	cipherSelection = ''
	requestedEnc = request.form.get('encMethod')
	requestedDec = request.form.get('decMethod')	

	if (request.method == "POST"):
		output = request.form.to_dict()
		message = output["message"] # retrieves message from text box

		# checks which cipher was selected
		if (requestedEnc == "Caesar Cipher"): #encrypting caesar cipher
			cipherSelection = "Encrypting Caesar Cipher: <br>"
			message = encCaesarCipher(message)
			results = cipherSelection + message
		elif (requestedEnc == "Reverse Cipher"): #encrypting reverse cipher
			cipherSelection = "Encrypting Reverse Cipher: <br>"
			message = encReverseCipher(message)
			results = cipherSelection + message
		elif (requestedEnc == "Homomorphic Encryption"): #homomorphic encryption
			s_bit1 = int(output["homomorphic-method-type-1"])
			s_bit2 = int(output["homomorphic-method-type-3"])
			a_bit1 = int(output["homomorphic-method-type-2"])
			a_bit2 = int(output["homomorphic-method-type-4"])
			message += str(s_bit1)
			message += str(s_bit2)
			message += str(a_bit1)
			message += str(a_bit2)
			results = str(homomorphicEnc(s_bit1, s_bit2, a_bit1, a_bit2))
		elif (requestedDec == "Caesar Cipher"): #decrypting caesar cipher
			cipherSelection = "Decrypting Caesar Cipher: <br>"
			message = str(decCaesarCipher(message))
			message = message.strip("}'{")
			message = message.replace(",", "<br>")
			results = cipherSelection + message
		elif (requestedDec == "Reverse Cipher"): #decrypting reverse cipher
			cipherSelection = "Decrypting Caesar Cipher: <br>"
			message = decReverseCipher(message)
			results = cipherSelection + message
		else:
			results = "Select an Encrytion/Decryption Method"
			
	return render_template("index.html", message = results)

# function to encrypt a caesar cipher message
def encCaesarCipher(msg):
	cipherMsg = ''
	shiftNum = random.randint(1, 26)

	# traverse through the message
	for i in range(len(msg)):
		char = msg[i]

		# Encrypt numbers
		if (char.isdigit()):
			char_new = (int(char) + shiftNum) % 10
			cipherMsg += str(char_new)

		# Encrypt uppercase characters
		elif (char.isupper()):
			cipherMsg += chr((ord(char) + shiftNum - 65) % 26 + 65)

        # Encrypt lowercase characters
		elif (char.islower()):
			cipherMsg += chr((ord(char) + shiftNum - 97) % 26 + 97)

		# Encrypt special characters
		else:
			cipherMsg += char
		
	return cipherMsg

# function to encrypt a reverse cipher message
def encReverseCipher(msg):
	cipherMsg = ''

	i = len(msg) - 1
	while (i >= 0):
		cipherMsg += msg[i]
		i -= 1
		
	return cipherMsg

# function to encrypt using homomorphic encryption
def homomorphicEnc(s_bit1, s_bit2, a_bit1, a_bit2):
	r1 = randint(1, 5)
	r2 = randint(1, 5)
	r3 = randint(1, 5)
	r4 = randint(1, 5)

	q1 = randint(50000, 60000)
	q2 = randint(50000, 60000)
	q3 = randint(50000, 60000)
	q4 = randint(50000, 60000)

	p = randint(10000, 20000) # private key
	
	# Equation: c = p*q + 2*r + m
	c_bit_bit1 = q1 * p + 2 * r1 + s_bit1
	c_bit_bit2 = q2 * p + 2 * r2 + s_bit2
	c_bit_bit3 = q3 * p + 2 * r3 + a_bit1
	c_bit_bit4 = q4 * p + 2 * r4 + a_bit2

	# Truth Table
	cipher_text = inv(c_bit_bit2)*c_bit_bit4 + inv(c_bit_bit2)*inv(c_bit_bit1)*c_bit_bit3 + inv(c_bit_bit1)*c_bit_bit4*c_bit_bit3

	truth_table = "R Values: "
	truth_table += str(r1) + " " + str(r2) + " " + str(r3) + " " + str(r4) + "<br>"
	truth_table += "Q Values: "
	truth_table += str(q1) + " " + str(q2) + " " + str(q3) + " " + str(q4) + "<br>"
	truth_table += "Private Key: "
	truth_table += str(p) + "<br><br>"

	truth_table += "Input Bits" + "<br>"
	truth_table += "---------------" + "<br>"
	truth_table += "s_bit1: " + "   " + str(s_bit1) + "&emsp;" + "s_bit2: " + "   " + str(s_bit2) + "<br>"
	truth_table += "a_bit1: " + "   " + str(a_bit1) + "&emsp;" + "a_bit2: " + "   " + str(a_bit2) + "<br><br>"

	truth_table += "Cipher Bits" + "<br>"
	truth_table += "---------------" + "<br>"
	truth_table += "A: " + "   " + str(c_bit_bit1) + "&emsp;" + "B: " + "   " + str(c_bit_bit2) + "<br>"
	truth_table += "C: " + "   " + str(c_bit_bit3) + "&emsp;" + "D: " + "   " + str(c_bit_bit4) + "<br><br>"

	truth_table += "Cipher Results" + "<br>"
	truth_table += "---------------" + "<br>"
	truth_table += "Cipher Text: " + "   " + str(cipher_text) + "<br><br><br>"

	# decrypt value
	resultingVal = "Resulting value: "
	result = (cipher_text % p) % 2
	resultingVal += str(result)

	# checks result
	if (result == 1):
		message = "Alexa has a higher salary than Siri"
	else:
		message = "Alexa is not richer than Siri"

	return truth_table + str(result) + "<br>" + message

# decrements value
def inv(val):
	return(val ^ 1)

# function to decrypt a caesar cipher message
def decCaesarCipher(msg):
	encryptedMsg = msg
	letters = "abcdefghijklmnopqrstuvwxyz"
	LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	shiftNum = random.randint(1, 26)
	x = 0
	decryptedDict = {}
	
	# iterates through all possibilities
	while x < 26:
		x += 1
		decString = ""
		# strToDecrypt = encryptedMsg.lower()
		strToDecrypt = encryptedMsg
		ciphershift = int(x)

		# iterates through each character of encrypted msg
		for char in strToDecrypt:
			if (char.isupper()):
				position = LETTERS.find(char)
			else:
				position = letters.find(char)
			newPosition = position - ciphershift
			
			# decrypts digits
			if (char.isdigit()):
				char_old = (int(char) - shiftNum) % 10
				decString += str(char_old)

			#decrypts characters
			elif char in LETTERS:
				decString += LETTERS[newPosition]
			elif char in letters:
				decString += letters[newPosition]
			
			# decrypts special characters
			else:
				decString += char
		
		ciphershift = str(ciphershift)
		decryptedDict[x] = decString

	return decryptedDict

# function to decrypt a reverse cipher message
def decReverseCipher(msg):
	decMsg = ''

	i = len(msg) - 1
	while (i >= 0):
		decMsg += msg[i]
		i -= 1
		
	return decMsg

if (__name__=='__main__'):
	app.run(debug=True)

