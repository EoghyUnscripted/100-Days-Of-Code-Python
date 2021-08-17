# Day 8 Caesar Cipher

### Instructions

1. Import and print the logo from art.py when the program starts.

2. What if the user enters a shift that is greater than the number of letters in the alphabet?
    1. Try running the program and entering a shift number of 45.
    2. Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    3. Hint: Think about how you can use the modulus (%).

3. What happens if the user enters a number/symbol/space?
    1. Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        
            e.g. start_text = "meet me at 3"
                 end_text = "•••• •• •• 3"

4. Can you figure out a way to ask the user if they want to restart the cipher program?
            
            e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
        
    1. If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    2. Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

### Example Gameplay
