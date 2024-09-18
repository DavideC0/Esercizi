from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

"""# Generating RSA Key Pair
key_pair = RSA.generate(2048)
public_key = key_pair.publickey()
with open("public_key.txt", "w") as f:
    f.write(str(public_key.export_key()))
with open("private_key.txt", "w") as f:
    f.write(str(key_pair.export_key()))"""


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")

"""#import key
with open("public_key.txt", "r") as f:
    public_key = RSA.import_key(f.read())
with open("private_key.txt", "r") as f:
    key_pair = RSA.import_key(f.read())"""
    
public_key = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzyQM3oTn3f0IkJcGKUdW\nw/NYB0fAvmcIP33ec1CN1McubLXvazpeO0yiJBJz3CkksbV6HkNFgsdKA5JBqU90\ngPxi0ilpBsJW8LnJq9eTmxwpKOBNGUtI/0yyONrqkG6DnkzqTN3OYbYkKXwcjQiE\nM53ivJ+meV3cEv06KpW1bzdjfBt9ZUW/yafdWeeunGKqTqmwvf670CgXdtTRhTHi\njP1zaZScVfj+HbcID+qzG+yUmKdAQHEsKnlZNiRipqEE6xHBid/LWXWH+6loXpbl\nO3luv0uJ8qfTV6rJGg3eiyZ+hDkFpAyW6D+xgN9Dmn+jOdw/sxgPaMb5PtZc+8fe\niwIDAQAB\n-----END PUBLIC KEY-----'
key_pair = '-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAzyQM3oTn3f0IkJcGKUdWw/NYB0fAvmcIP33ec1CN1McubLXv\nazpeO0yiJBJz3CkksbV6HkNFgsdKA5JBqU90gPxi0ilpBsJW8LnJq9eTmxwpKOBN\nGUtI/0yyONrqkG6DnkzqTN3OYbYkKXwcjQiEM53ivJ+meV3cEv06KpW1bzdjfBt9\nZUW/yafdWeeunGKqTqmwvf670CgXdtTRhTHijP1zaZScVfj+HbcID+qzG+yUmKdA\nQHEsKnlZNiRipqEE6xHBid/LWXWH+6loXpblO3luv0uJ8qfTV6rJGg3eiyZ+hDkF\npAyW6D+xgN9Dmn+jOdw/sxgPaMb5PtZc+8feiwIDAQABAoIBACfCEKJJOkP2hEVU\nZ39WzQWRWI0VLZ6eIgwluaPCi2aS0ItXJFwdeObC38AytoBEeWGOpqDWYqomXENx\nOB8qO/9h8gnKnvkIJi3QSzArkY5NCm1pGANJ2vn9m5ukES+ltqeUtcgJLsq8bhZ0\nVvqO7ukFXfa8YfSbmlket6Ji188/ptUf3W5atC9bII0DMrdWjWy7tTQkzHaA4XTN\nwWqsjIsL8llvjOfdXFDuG2N9LrYh9pMC1AWlTLsJqnZPBuPapSjj37H9JbgvSMV3\nZeRY7PW+IRZfLLmF5zozH4On8gjKseZ5qvosulmxAuVoqecUT2Umf1QWQpvz5Bm2\nxtnrxkECgYEA2e9mrnNx1IPXgX8k5ic8bHsd9av08jg4m8d5X8Pw3nGjQwjPWME7\nhB4LP3/0F/AB5e8ed3DOEvWemtDWlyFCF1E8DURBoMuZwKBXd6H8X5QSEAXv+anZ\nHu8mbp0UXqyohbOymWuQ+9Rqkb8PzVD1aS4rTUnejkcogYl0Bn7WvOECgYEA81H/\nq3e8tR3RLLz97f64IAF553rt35ZSG1Pfmgq5IB5atcYFTYY+mjWDHWpc2O57h2zh\nBv7I4iD2jcwRgpq6lyhgCnux1ONvnK9Y9E2sBJzRutL+vS+J4aW020vrHgud2TSU\nzUzHdwwH0+YgT87bhVYeTjRHWXuFbzB4xh8b/OsCgYBZCyjAFGko9Glj/qf75YIZ\nrMAT9ZtSMEho1bqwtyU+Ld4P8JSPZfxEQeZEnqoD8ctEwEuJb6yzMGoKRVO4Uh1n\n24gWv5G0+hsrChhSx/uOrbgnldV0A8KzkfD49vMwr4j3f/F0H/AQBL06KX9yWya6\nP+PvY0Qsi8RwENI4KTDh4QKBgGfJ+2f1vD35iQcvWpWRSJMGbixqSFtOMJnNjhyU\nJGFp8UGGRS7La5q15sa+Xvp9x519uQMV3TRv4RudB38RZzQhGc5+8t0fYrWQKj6T\nfyO8jM3HQLgMNiFVYK8GVDVNuTg0cKCd9pt2O0SM7g187DCVCnpLXH/z63gBUhMY\npASfAoGAMaHUD7Y/PQlgS8FHflpKiehZyUSpvfQ+0RuLO/YfrS70dMU243htE66k\nZCVM3PKYbKteliGeLEbaI5lSdL4HNpMwUFyqH+duopEBbMez0EgtUdNs8oUzPQd7\nc2BiBvV7y7pZBELM+PLPkGOfZyFjD17ltN4K9VHcmqFm2ArLnd4=\n-----END RSA PRIVATE KEY-----'

public_key = RSA.import_key(public_key)
key_pair = RSA.import_key(key_pair)
# Example usage
message = "This is a secret message"
encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)