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
	if (request.method == "POST"):
		output = request.form.to_dict()
		message = output["message"]

	return render_template("index.html", message = 'Encrypted ' + message)

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
