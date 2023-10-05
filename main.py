alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

def caesar(input_text,shift_amount,direct):
  requried_text = ""
  for letter in input_text:
    position = alphabet.index(letter)
    if direct == 'encode':
      if position >= 25:
        position = position%25 -1
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      requried_text += new_letter
    else:
      if position < 0:
        position = position+25 -1
      new_position  = position - shift_amount
      new_letter = alphabet[new_position]
      requried_text += new_letter
  print(f"Here's the {direction}d result: {requried_text}")
  
should_continue = True
while should_continue:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text,shift,direction)
  next = input("\nDo you want to continue? type 'yes' to continue or type 'no' to stop.\n").lower()

  if next == "no":
    should_continue = False
    print("Goodbye.")
  

# def encrypt(plain_text,shift_amount):
#   cipher_text = ""
#   for letters in plain_text:
#     position = alphabet.index(letters)
#     if position >= 25:
#       position = position%25 - 1
#     new_position = position + shift_amount
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text , shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     if position < 0:
#       position = position+25 -1
#     new_position  = position - shift_amount
#     new_letter = alphabet[new_position]
#     plain_text += new_letter
#   print(plain_text)

 
# if direction == 'encode':
#   encrypt(text,shift)
# else:
#   decrypt(text,shift)
