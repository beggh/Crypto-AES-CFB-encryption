
from Crypto.Cipher import AES
import binascii,os            
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from Crypto.Hash import SHA256
from Crypto import Random

#password=input("Enter passw: ")

#print(password)

#hash_obj=SHA256.new(password.encode('utf-8'))
hkey=b'\x18_\x8d\xb3"q\xfe%\xf5a\xa6\xfc\x93\x8b.&C\x06\xec0N\xdaQ\x80\x07\xd1vH&8\x19i'
#print(hkey)

#def pad(s):
    #return s+b"\0" *((AES.block_size-len(s)) % AES.block_size)

def encrypt(msg,hkey):
    #msg=pad(msg)
    iv=Random.new().read(AES.block_size)
    cipher=AES.new(hkey,AES.MODE_CFB,iv)
    #result=cipher.encrypt(padding(msg).encode('utf-8'))
    return iv+cipher.encrypt(msg)
#e2.insert(0,ans)
msg="I love python too much forever"
ans=encrypt(msg,hkey)
print(ans)


def decrypt(cyphertext,hkey):
    iv=cyphertext[:AES.block_size]
    decipher=AES.new(hkey,AES.MODE_CFB,iv)
    plaint=decipher.decrypt(cyphertext[AES.block_size:]).decode('utf-8')
    #pad_index=plaint.find(PAD)
    #result=plaint[:pad_index]
    return plaint
    #e4.insert(0,result)
    
res=decrypt(ans,hkey)
print(res)    
filename=None 

def encrypt_file(file_name,hkey):
    with open(file_name,'br') as f:
        plaintext=f.read()
    enc=encrypt(plaintext,hkey)    
    with open(file_name+".enc",'bw') as f:
        f.write(enc)


def decrypt_file(file_name,hkey):
    with open(file_name,'br') as f:
        cyphertext=f.read()
    dec=decrypt(cyphertext,hkey)
    with open(file_name[:-4],'w') as f:
        f.write(dec)


def load_file():
    global hkey,filename
    text_file=filedialog.askopenfile(filetypes=[('Text Files','txt')])
    if text_file.name!=None:
        filename=text_file.name
        
        

def encrypt_the_file():
    global hkey,filename
    if filename!=None:
        encrypt_file(filename,hkey)
    else:
        messagebox.showerror(title="Error:",message="There was no file loaded to encrypt")
        

def decrypt_the_file():
    global hkey,filename
    if filename!=None:
        fname=filename+".enc"
        decrypt_file(fname,hkey)
    else:
        messagebox.showerror(title="Error:",message="There was no file loaded to encrypt")
    

root=tkinter.Tk()
root.title("CRYPTOGRAPHY") 
root.geometry("300x300") 
loadButton=tkinter.Button(root,text="Load Text File",bg ="blue", fg ="white",command=load_file)
encryptButton=tkinter.Button(root,text="Encrypt Text File",bg ="red", fg ="white",command=encrypt_the_file)
decryptButton=tkinter.Button(root,text="Decrypt Text File",bg ="green", fg ="white",command=decrypt_the_file)

loadButton.pack()
encryptButton.pack()
decryptButton.pack()

root.mainloop()

