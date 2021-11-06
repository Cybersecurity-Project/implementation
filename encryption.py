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
	print(requestedEnc)
	
	if (request.method == "POST"):
		output = request.form.to_dict()
		message = output["message"]

		# checks which cipher was selected
		if (requestedEnc == "Caesar Cipher"):
			cipherSelection = "Caesar Cipher: "
			message = caesarCipher(message)
			print(message)
		elif (requestedEnc == "Reverse Cipher"):
			cipherSelection = "Reverse Cipher: "
			message = reverseCipher(message)
			print(message)
		else:
			print("hello")
			

	return render_template("index.html", message = 'Encrypted ' + cipherSelection + message)

# function to produce a caesar cipher message
def caesarCipher(msg):
	cipherMsg = ''
	shiftNum = 4

	# traverse through the message
	for i in range(len(msg)):
		char = msg[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			cipherMsg += chr((ord(char) + shiftNum - 65) % 26 + 65)
        # Encrypt lowercase characters
		else:
			cipherMsg += chr((ord(char) + shiftNum - 97) % 26 + 97)
		
	return cipherMsg
	# return render_template("index.html", message = "Hello")

# function to produce a reverse cipher message
def reverseCipher(msg):
	cipherMsg = ''

	i = len(msg) - 1
	while (i >= 0):
		cipherMsg += msg[i]
		i -= 1
		
	return cipherMsg

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
