# contiguous_chain
Python Test

Required: Python 2.7


Description:

If something is contiguous, it means it is connected or unbroken. For a chain, this would mean that all parts of the chain are reachable without leaving the chain. So, in this little piece of ASCII-art:
xxxxxxxx  
x      x
there is only 1 contiguous chain, while in this
xxxx xxxx 

x
there are 3 contiguous chains. Note that a single x, unconnected to any other, counts as one chain.
For the purposes of this problems, chains can only be contiguous if they connect horizontally of vertically, not diagonally. So this image
xx
  xx
    xx    
contains three chains.
Your challenge today is to write a program that calculates the number of contiguous chains in a given input.
Formal inputs & outputs

Input:

The first line in the input will consist of two numbers separated by a space, giving the dimensions of the ASCII-field you're supposed to read. The first number gives the number of lines to read, the second the number of columns (all lines have the same number of columns).
After that follows the field itself, consisting of only x's and spaces.
Output:

Output a single number giving the number of contiguous chains.
Sample inputs & outputs

Input 1

2 8
xxxxxxxx
x      x
Output 1

1
Input 2

3 9
xxxx xxxx
    x    
   xx    
Output 2

3
Challenge inputs:

Input 1

4 9
xxxx xxxx
   xxx   
x   x   x
xxxxxxxxx
Input 2

8 11
xx x xx x  
x  x xx x  
xx   xx  x 
xxxxxxxxx x
         xx
xxxxxxxxxxx
 x x x x x 
  x x x x