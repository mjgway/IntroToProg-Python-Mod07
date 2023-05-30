# IntroToProg-Python-Mod07
## Assignment 07  
### Binary to File with Error Handling (Python)  
 
**Introduction**  

This week’s module 7 we were introduced to the concept of readlines function, reading multiple rows, combining read/write, working with binary files using pickling and creating exception class for structured error handling. For assignment 07 we were asked to make revisions to an incomplete script that saved data from memory to file in binary format, read the binary back and experiment with error handling. 

My first task was to format my script into import, data, processing, and presentation sections. The original script called for an import of binary pickle data, so I set variables and created a class called Processor which would append and read to the data file in binary form. Writing in binary is a good way to store data for multiple formats and reduce file size, although it is not encrypted so it should not be used to store important data. I defined a save data file to append in binary ‘ab’ and a defined read data file in binary ‘rb’. My presentation collected input data to memory and returned the data back to the user, storing the list object and displaying the data from file from a new list object. Lastly, I experimented with structured error handling using Python standard errors, setting a try, if raise, except conditions to alert the user that an error occurred when trying to create a new file name. 

![image](https://github.com/mjgway/IntroToProg-Python-Mod07/assets/133425498/42ac316c-acc8-4451-9f6e-f39679507903)
* *Figure 1.0 | Class Processor with Binary ‘AB’* *

I validated my script by running the program in PyCharm to ensure the program was writing to the txt file and no other issues were found. Next, I opened Python in the Windows command shell and entered my directory script location. Once I got a clean pass-through without any errors, I saved the script to my Assignment03 subfolder in the _PythonClass folder on my C: drive. I also added my file to GitHub and posted it for the class on the discussion board.

**Summary**  

If I had more time on this assignment I would have made significant improvements to presentation, for instance: add class with defined menu choice, created a while loop for easy user entry, set conditions for menu options, added custom error handling to control end user entries. Overall, I found the coding to read and write in binary to be not too challenging and error handling to be challenging because of all the possible errors a user entry could elicit from the script. 

