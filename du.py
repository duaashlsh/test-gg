def caser(plaintext,shaft):
    ciphertext=""
    for i in plaintext:
        if i .isalpha():
            m=ord(i) +shaft
            if m > ord("z"):
                m-=26
            u=chr(m)
        ciphertext+=u
    print("your ciphertext is",ciphertext)
caser("hello",6)
# nkrru هذا طلع ناتج تشفير
def d_caser(ciphertext,shaft):
    plaintext=""
    for i in ciphertext:
        if i .isalpha():
            m=ord(i) -shaft
            if m > ord("z"):
                m+=26
            u=chr(m)
        plaintext+=u
    print("your plaintext is",plaintext)
d_caser("nkrru",6)
#your ciphertext is nkrru\هذا ناتج دالتين 
#your plaintext is hello
