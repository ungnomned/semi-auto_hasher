# semi-auto_hasher WINDOWS ONLY
Python must be installed for this program to work.
This incredibly simple program is meant to help speed up the process of verifying hashes mosstly by eliminating the manual work of comparing them with your eyes.
simply enter: the path of the item you want to generate a hash for, 
              the type of hash you want to generate,  
              the trusted hash you obtained from the website you downloaded from, 
              
The program will generate a hash and compare it to the one you pasted in and then send either a green light for hashes that match or red light for hashes that don't.
#INSTRUCTIONS (Windows Only)

1. Download the hasher.py file and save to desired location
2. Open a text editor and create a batch file with the following

3. @ECHO OFF
4. cd "Full path to hasher.py location" e.g. cd C:\Users\guest\Downloads
5. START python hasher.py

6. Save the text document as a .bat file preferably somewhere on the desktop for easy accesibility
