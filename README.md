# __Processing Encrypted Data__

## _Graphical User Interface:_
[Processing Encrypted Data](http://52.91.201.108:8080/)

## _Overview:_
This is a simple graphical user interface (GUI) that allows users to be able to view how certain encryption schemes work. This webpage was created with the use of HTML, CSS, and JavaScript. For implementation of the encryption schemes, Python was the main programming language as it had many packages to utilize. We also used Flask, a Python framework that made it possible to display our Python code to our web page. The main encryption algorithms used in the webpage are Caesar Cipher, Reverse Cipher, and Homomorphic Encryption. Another file called “scriptEncryption.py” in the repository is an algorithm for using AES to encrypt local files on your computer. 

***AES Encryption of Files:*** <br />
The file of “scriptEncryption.py” can be opened as an executable file. It will prompt the user to enter a password that will be used for decrypting later on. Once entered, it will need to be restarted to allow an encrypted password file to be created. Then the file can be opened again and the user will be able to select any files within the root of the executable file to encrypt. Individual files or all files within the root can be encrypted. The user may also select to decrypt the files as well if the password entered is correct. This provides a simple overview of how AES can be used when encrypting files/folders within local computers.

***Webpage:*** <br />
Users will be able to type out any message they would like in the text box to the left and select an encryption/decryption method from the dropdown menu. Caesar and Reverse Ciphers are simple schemes that involve shifting of the letters. For decrypting Caesar Cipher, a brute force method is used to view all possible combinations in retrieving the original message. For Homomorphic Encryption, it is a basic interactive example to define the salaries of Alexa and Siri in a two-bit binary value. The mathematics behind the scheme uses the fully homomorphic encryption scheme of DGHV (Dijk, Gentry, Halevi, and Vaikuntanathan) from their [paper](https://eprint.iacr.org/2009/616.pdf). 

***Viewing Project*** <br />
To view the code within the project, clone the repository. Ensure to have the following installed:
* Python
* Python packages:
  * pip install virtualenv
  * pip install flask
  * pip install pycryptodomex

To open up the graphical user interface in a local server, go into the folder in the terminal. Type:

```py encryption.py```

This will display the ip address of where the project is running on. Click on the link to view the web page and perform any of the encryption schemes that are implemented.

