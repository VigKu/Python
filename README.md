
---
## Passwork Checker

Given a string, write a function to determine if it is a legitimate *Password*, satisfying the following conditions: 
- (i) length between 8 and 24,    
- (ii) at least one uppercase character,    
- (iii) at least one lowercase character,    
- (iv) at least one digit,     
- (v) at least one special character amongst `!@#%&*`, and    
- (vi) no spaces in between.      

The function should accept a `string` as input, and return `True` or `False` according to the conditions.     
You may want to check all "methods" (functions) in the `string` class to find the ones you need in this case.

---
## Count Word Frequencies

Given an input text file, record the *Count/Frequency* of all words longer than 3 characters in a Dictionary `{word: count}`, and sort it by Count/Frequency. 

---
## Levenshtein Distance

Given two strings as User input, write a function to compute the *Levenshtein Distance* (https://en.wikipedia.org/wiki/Levenshtein_distance) between them. 

---
## Convolution Filtering

In image processing, several operations (blurring, sharpening, embossing, edge detection, etc.) can be accomplished by doing a **convolution between a kernel and an image**, where the Kernel or Mask (https://en.wikipedia.org/wiki/Kernel_(image_processing)) refers to a small ($3 \times 3$, say) numeric matrix.


Import `poDumpling.jpg` using NumPy, convert it to Grayscale, as in `Chapter5_PythonComputing`, and choose any $3 \times 3$ kernel for processing the image (from https://en.wikipedia.org/wiki/Kernel_(image_processing)). Apply the chosen kernel as a *convolution filter* on the Grayscale image to accomplish the target image processing task (one out of blurring, sharpening, embossing, edge detection), and show the final result. Use *only* NumPy in this process.
