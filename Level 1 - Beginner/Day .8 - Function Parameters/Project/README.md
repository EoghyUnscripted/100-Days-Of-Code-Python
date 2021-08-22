# Day 8 Caesar Cipher

## Caesar Cipher Part 1: Encryption

### Instructions

1. Create a function called `encrypt` that takes the 'text' and 'shift' as inputs.
2. Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
3. Call the 'encrypt' function and pass in the user inputs. You should be able to test the code and encrypt a message.

#### Code

Use the provided code to complete the project.

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    # TODO Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  

# TODO Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
```

### Example Input

    Type your message: hello
    Type the shift number: 5

### Example Output

    The encoded text is mjqqt

### Hint

How do you get the index of an item in a list: [Finding the index of an item in a list](https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list)

**Bug alert:** What happens if you try to encode the word 'civilization'?

## Caesar Cipher Part 2: Decryption

### Instructions

1. Create a different function called `decrypt` that takes the 'text' and 'shift' as inputs.
2. Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
3. Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
    1. Then call the correct function based on that 'drection' variable.
    2. You should be able to test the code to encrypt *AND* decrypt a message.

#### Code

Use the provided code to complete the project.

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

# TODO Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  # TODO Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  

# TODO Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
encrypt(plain_text=text, shift_amount=shift)
```

### Example Input

    Type 'encode' to encrypt, type 'decode' to decrypt: decode
    Type your message: mjqqt
    Type the shift number: 5

### Example Output

    The decoded text is hello

## Caesar Cipher Part 3: Reorganising the Code

### Instructions

1. Combine the encrypt() and decrypt() functions into a single function called caesar().
2. Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

#### Code

Use the provided code to complete the project.

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)

# TODO Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
```
