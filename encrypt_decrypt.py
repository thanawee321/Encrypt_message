from cryptography.fernet import Fernet
import argparse

def create_key():
    key = Fernet.generate_key()
    return key

def encrypt(key, message):
    f = Fernet(key)
    token = f.encrypt(message.encode())
    return token

def decrypt(key, token):
    f = Fernet(key)
    message = f.decrypt(token.encode())
    return message

def main(args):
    if args.create:
        key = create_key()
        print("🔑 Generated Key:", key.decode())
        return

    if args.encrypt and args.message and args.key:
        token = encrypt(args.key.encode(), args.message)
        print("🔐 Encrypted:", token.decode())
        return

    if args.decrypt and args.key and args.message:
        try:
            message = decrypt(args.key.encode(), args.message)
            print("🔓 Decrypted:", message.decode())
        except Exception as e:
            print("❌ Decryption failed:", e)
        return

    print("⚠️  Invalid usage. Use --help to see available options.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--create', action='store_true', help="Generate a new key")
    parser.add_argument('-m','--message', help="Message to encrypt or decrypt")
    parser.add_argument('-key','--key', help="Base64-encoded Fernet key")
    parser.add_argument('-e','--encrypt', action='store_true', help="Encrypt the message")
    parser.add_argument('-d','--decrypt',action='store_true', help="Decrypt the message")
    args = parser.parse_args()
    main(args)
