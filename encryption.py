from cryptography.fernet import Fernet

# importing Flask and other modules
from flask import Flask, request, redirect, render_template, flash

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

		# checks which cipher was selected
		if (requestedEnc == "Caesar Cipher"): #encrypting caesar cipher
			cipherSelection = "Encrypting Caesar Cipher: "
			message = encCaesarCipher(message)
			print(message)
		elif (requestedEnc == "Reverse Cipher"): #encrypting reverse cipher
			cipherSelection = "Reverse Cipher: "
			message = encReverseCipher(message)
			print(message)
		elif (requestedDec == "Caesar Cipher"): #decrypting caesar cipher
			cipherSelection = "Decrypting Caesar Cipher: <br>"
			message = str(decCaesarCipher(message))
			message = message.strip("'{")
			message = message.replace(",", "<br>")
			# message = message.replace(",", "\n")
			print(message)
		elif (requestedDec == "Reverse Cipher"): #decrypting reverse cipher
			cipherSelection = "Decrypting Caesar Cipher: <br>"
			message = decReverseCipher(message)
			print(message)
		else:
			print("Select an Encryption/Decryption Scheme")
			
	return render_template("index.html", message = cipherSelection + message)

# function to encrypt a caesar cipher message
def encCaesarCipher(msg):
	cipherMsg = ''
	shiftNum = 4

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

# function to decrypt a caesar cipher message
def decCaesarCipher(msg):
	encryptedMsg = msg
	letters = "abcdefghijklmnopqrstuvwxyz"
	shiftNum = 4
	x = 0
	decryptedDict = {}
	
	# iterates through all possibilities
	while x < 26:
		x += 1
		decString = ""
		strToDecrypt = encryptedMsg.lower()
		ciphershift = int(x)

		# iterates through each character of encrypted msg
		for char in strToDecrypt:
			position = letters.find(char)
			newPosition = position - ciphershift
			
			# decrypts digits
			if (char.isdigit()):
				char_old = (int(char) - shiftNum) % 10
				decString += str(char_old)

			#decrypts characters
			elif char in letters:
				decString += letters[newPosition]
			
			# decrypts special characters
			else:
				decString += char
		
		ciphershift = str(ciphershift)
		# print(decString)
		decryptedDict[x] = decString
	# print(decryptedDict)
		# print("You used a cipher shift of " + ciphershift)
		# print("Your decrypted message reads: ")
		# print(decString)
		# print("\n")
	# print(decString, "124")
	# print("\n")

	return decryptedDict

# function to decrypt a reverse cipher message
def decReverseCipher(msg):
	decMsg = ''

	i = len(msg) - 1
	while (i >= 0):
		decMsg += msg[i]
		i -= 1
		
	return decMsg

# edited out for now
def encryption2():
	message = ''
	if (request.method == "POST"):
		# # getting input with name = fname in HTML form
		message = request.form.get("message")
		print(message)
		# print(first_name + "\n")
		# # getting input with name = lname in HTML form
		# last_name = request.form.get("lname")
		# print(last_name)
 
		# # generate a key for encryption and decryption 
		# key = Fernet.generate_key()
		
		# # Fernet class with the key
		# fernet = Fernet(key)
		
		# # string must be encoded to byte string before encryption
		# encMessage = fernet.encrypt(message.encode())
		
		# print("Original string: ", message)
		# print("Encrypted string: ", encMessage)
		
		# # Decode string with decode methods
		# decMessage = fernet.decrypt(encMessage).decode()
		
		# print("decrypted string: ", decMessage)

		#return "Encrypted " + message 
	return render_template("index.html", message = "Encrypted " + message)

if (__name__=='__main__'):
	app.run(debug=True)
