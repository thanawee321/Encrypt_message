import argparse
import pyperclip
import os
from cryptography.fernet import Fernet

class Encryption:
    
    
    
    def Create(self):
        key = Fernet.generate_key()
        return key
    
    def Encrypt(self,key,message):
        f = Fernet(key)
        token = f.encrypt(message.encode())
        return token
    
    def Decrypt(self,key,token):
        f = Fernet(key)
        message = f.decrypt(token.encode())
        return message
    
    
def main(args):
    
    if args.create:
        create = Encryption()
        key = create.Create()
        print("🔑 Generated Key:", key.decode())
        try:
            pyperclip.copy(key.decode())
            print("📋 Key copied to clipboard!")
        except:
            os.system(f'echo "{key.decode()}" | xclip -selection clipboard')
            
        return 
    
    if args.encrypt and args.message and args.key:
        encrypt = Encryption()
        token = encrypt.Encrypt(args.key.encode(),args.message)
        print("🔐 Encrypted:", token.decode())
        try:
            pyperclip.copy(token.decode())
            print("📋 Encrypted token copied to clipboard!")
        except:
            os.system(f'echo "{token.decode()}" | xclip -selection clipboard')
            
        return 
        
    if args.decrypt and args.message and args.key:
        decrypt = Encryption()
        try:
            message = decrypt.Decrypt(args.key,args.message)
            print("🔓 Decrypted:", message.decode())
            try:
                pyperclip.copy(message.decode())
                print("📋 Decrypted message copied to clipboard!")
            except:
                
                os.system(f'echo "{message.decode()}" | xclip -selection clipboard')
                
        except Exception as e:
            print("❌ Decryption failed:", e)
        return
            
        
        
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    logo_lines = [
        
        " ██████╗    █████╗   ██████╗  ██╗   ██╗ ██╗  ██╗  ██████╗   ██████╗  ██╗  ██╗",
        " ██╔══██╗  ██╔══██╗  ██╔══██╗ ╚██╗ ██╔╝ ██║  ██║ ██╔═══██╗ ██╔═══██╗ ██║ ██╔╝",
        " ██████╔╝  ███████║  ██████╔╝  ╚████╔╝  ███████║ ██║   ██║ ██║   ╚═╝ █████═╝ ",
        " ██╔══██╗  ██╔══██║  ██╔══██╗   ╚██╔╝   ██╔══██║ ██║ █ ██║ ██║       ██╔ ██╗ ",
        " ██████╔╝  ██║  ██║  ██████╔╝    ██║    ██║  ██║ ██║ ████║ ██║   ██╗ ██╔══██╗",
        " ╚═════╝   ╚═╝  ╚═╝  ╚═════╝     ╚═╝    ╚═╝  ╚═╝  ╚══╝╚══╝ ╚██████╔╝ ╚═╝  ╚═╝",
        "                                                    (CRYPTOGRAPHY V1.0.0)"
    ]
    
    for line in logo_lines:
        print(line)
        
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--create', action='store_true', help="Generate a new key(s)")
    parser.add_argument('-m','--message',help="Message to encrypt or decrypt(if you want decrypt the message is a Token)")
    parser.add_argument('-key','--key', help="Base64-encoded Fernet key")
    parser.add_argument('-e','--encrypt', action='store_true', help="Encrypt the message")
    parser.add_argument('-d','--decrypt',action='store_true', help="Decrypt the message")
    args = parser.parse_args()
    
    main(args)