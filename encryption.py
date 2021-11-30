from re import A
from cryptography.fernet import Fernet

# importing Flask and other modules
from flask import Flask, request, redirect, render_template, flash
import random, sys
from random import randint

# import AES
from Crypto.Cipher import AES
from secrets import token_bytes

from flask.sessions import NullSession

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
		message = output["message"]
		print(output)
		# print(output["homomorphic-method-type-1"])

		# if (requestedEnc == "AES"):
		# 	nonce, cipherText, tag = encAES(message)
		# 	print(nonce)
		# 	print(cipherText)
		# 	print(tag)

		# checks which cipher was selected
		if (requestedEnc == "Caesar Cipher"): #encrypting caesar cipher
			cipherSelection = "Encrypting Caesar Cipher: <br>"
			message = encCaesarCipher(message)
			results = cipherSelection + message
			print(message)
		elif (requestedEnc == "Reverse Cipher"): #encrypting reverse cipher
			cipherSelection = "Encrypting Reverse Cipher: <br>"
			message = encReverseCipher(message)
			results = cipherSelection + message
			print(message)
		elif (requestedEnc == "Homomorphic Encryption"): #homomorphic encryption
			print('homomorphic encryption')
			bit1 = int(output["homomorphic-method-type-1"])
			bit2 = int(output["homomorphic-method-type-3"])
			bit3 = int(output["homomorphic-method-type-2"])
			bit4 = int(output["homomorphic-method-type-4"])
			message += str(bit1)
			message += str(bit2)
			message += str(bit3)
			message += str(bit4)
			print(message)
			results = str(homomorphicEnc(bit1, bit2, bit3, bit4))

			# cipherSelection = "Encrypting Using AES: <br>"
			# results = cipherText
			# print(cipherText)
		elif (requestedDec == "Caesar Cipher"): #decrypting caesar cipher
			cipherSelection = "Decrypting Caesar Cipher: <br>"
			message = str(decCaesarCipher(message))
			message = message.strip("}'{")
			message = message.replace(",", "<br>")
			results = cipherSelection + message
			# print(message)
		elif (requestedDec == "Reverse Cipher"): #decrypting reverse cipher
			cipherSelection = "Decrypting Caesar Cipher: <br>"
			message = decReverseCipher(message)
			results = cipherSelection + message
			print(message)
		# elif (requestedDec == "Homomorphic Decryption"): #homomorphic decryption
		# 	print("homomorphic decryption")
		# 	cipherSelection = "Decrytion of AES: <br>"
		# 	plaintext = decAES(nonce, cipherText, tag)
		# 	results = plaintext
		# 	print(plaintext)
		else:
			results = "Select an Encrytion/Decryption Method"
			print("Select an Encryption/Decryption Scheme")
			
	return render_template("index.html", message = results)

# function to encrypt a caesar cipher message
def encCaesarCipher(msg):
	cipherMsg = ''
	shiftNum = random.randint(1, 26)
	print(shiftNum)

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
	# return render_template("index.html", message = "Hello")

# function to encrypt a reverse cipher message
def encReverseCipher(msg):
	cipherMsg = ''

	i = len(msg) - 1
	while (i >= 0):
		cipherMsg += msg[i]
		i -= 1
		
	return cipherMsg

# function to encrypt using AES
def encAES(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    cipherText, tag = cipher.encrypt_and_digest(msg.encode('ascii')) #takes msg as bytes
    return nonce, cipherText, tag

# function to encrypt using homomorphic encryption
def homomorphicEnc(bit1, bit2, bit3, bit4):
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
	c_bit_bit1 = q1 * p + 2 * r1 + bit1
	c_bit_bit2 = q2 * p + 2 * r2 + bit2
	c_bit_bit3 = q3 * p + 2 * r3 + bit3
	c_bit_bit4 = q4 * p + 2 * r4 + bit4

	# Truth Table
	cipher_text = inv(c_bit_bit2)*c_bit_bit4 
	+ inv(c_bit_bit2)*inv(c_bit_bit1)*c_bit_bit3 
	+ inv(c_bit_bit1)*c_bit_bit4*c_bit_bit3

	truth_table = "R Values: "
	truth_table += str(r1) + " " + str(r2) + " " + str(r3) + " " + str(r4) + "<br>"
	truth_table += "Q Values: "
	truth_table += str(q1) + " " + str(q2) + " " + str(q3) + " " + str(q4) + "<br>"
	truth_table += "Private Key: "
	truth_table += str(p) + "<br><br>"

	truth_table += "Input Bits" + "<br>"
	truth_table += "---------------" + "<br>"
	truth_table += "Bit 1: " + "   " + str(bit1) + "&emsp;" + "Bit 2: " + "   " + str(bit2) + "<br>"
	truth_table += "Bit 3: " + "   " + str(bit3) + "&emsp;" + "Bit 4: " + "   " + str(bit4) + "<br><br>"

	truth_table += "Cipher Bits" + "<br>"
	truth_table += "---------------" + "<br>"
	truth_table += "A: " + "   " + str(c_bit_bit1) + "&emsp;" + "B: " + "   " + str(c_bit_bit2) + "<br>"
	truth_table += "C: " + "   " + str(c_bit_bit3) + "&emsp;" + "D: " + "   " + str(c_bit_bit4) + "<br><br>"

	truth_table += "Cipher Results" + "<br>"
	truth_table += "---------------" + "<br>"
	truth_table += "Result: " + "   " + str(cipher_text) + "<br><br>"

	print("R Values:\t", r1, r2, r3, r4)
	print("Q Values:\t", q1, q2, q3, q4)
	print("P Value:\t", p)

	print("\nInput Bits")
	print("---------------")
	print("bit1:\t", bit1, "bit2:\t", bit2)
	print("bit3:\t", bit3, "bit4:\t", bit4)

	print("\nCipher Bits")
	print("---------------")
	print("a:\t", c_bit_bit1, "b:\t", c_bit_bit2)
	print("c:\t", c_bit_bit3, "d:\t", c_bit_bit4)

	print("\nCipher Result")
	print("---------------")
	print("Result:\t", cipher_text)

	# decrypt value
	result = (cipher_text % p) % 2

	# checks result
	if (result == 0):
		print("Siri does not have a higher salary than Alexa")
		message = "Siri is not richer than Alexa"
	else:
		print("Siri is richer than Alexa")
		message = "Siri is richer than Alexa"

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
	print(shiftNum)
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

# function to decrypt an encrypted msg of AES
def decAES(nonce, cipherText, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
    plaintext = cipher.decrypt(cipherText)

    try:
        cipher.verify(tag)
        return plaintext.decode('ascii') # decodes the text
    except:
        return False

# edited out for now
# def encryption2():
# 	message = ''
# 	if (request.method == "POST"):
# 		# # getting input with name = fname in HTML form
# 		message = request.form.get("message")
# 		print(message)
# 		# print(first_name + "\n")
# 		# # getting input with name = lname in HTML form
# 		# last_name = request.form.get("lname")
# 		# print(last_name)
 
# 		# # generate a key for encryption and decryption 
# 		# key = Fernet.generate_key()
		
# 		# # Fernet class with the key
# 		# fernet = Fernet(key)
		
# 		# # string must be encoded to byte string before encryption
# 		# encMessage = fernet.encrypt(message.encode())
		
# 		# print("Original string: ", message)
# 		# print("Encrypted string: ", encMessage)
		
# 		# # Decode string with decode methods
# 		# decMessage = fernet.decrypt(encMessage).decode()
		
# 		# print("decrypted string: ", decMessage)

# 		#return "Encrypted " + message 
# 	return render_template("index.html", message = "Encrypted " + message)

if (__name__=='__main__'):
	app.run(debug=True)

