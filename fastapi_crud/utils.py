# Hashes a plain password using the bcrypt algorithm for secure storage.
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash(password:str):
    return pwd_context.hash(password)

#Verifies that a plain password matches the previously hashed password using bcrypt.
def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


