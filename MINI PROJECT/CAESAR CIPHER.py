alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_shift=(position+shift_key)%26 ##to get rid of list out of index 
            cipher_text+=alphabet[new_shift]
        else:
            cipher_text+=char
    print(f"here is the text after encryption: {cipher_text}")
def decrypt(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_shift=(position-shift_key)%26 ##to get rid of list out of index 
            plain_text+=alphabet[new_shift]
        else:
            plain_text+=char
    print(f"here is the text after encryption: {plain_text}")
wanna_end=False
while not wanna_end:
    what_to_do=input("TYPE 'encrypt' FOR ENCRYPTION TYPE 'decrypt' FOR DECRYPTION:")
    text=input("TYPE YOUR MESSSAGE:")
    shift=int(input("TYPE THE SHIFT NUMBER:"))
    if what_to_do=="encrypt":
        encrypt(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decrypt(cipher_text=text,shift_key=shift)
    play_again=input("enter 'yes' to continue or 'no' to discard:")
    if play_again=='no':
        wanna_end=True #######flip the condtion
        print("have a nice day! byee")
        