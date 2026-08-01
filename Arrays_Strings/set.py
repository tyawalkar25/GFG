from loguru import logger

email = ["tyawalkar3@gmail.com", "amrutapandejaipur@gmail.com"]

def encode_email(email):
    email_components = email.split("@")
    user_name = email_components[0]
    encoded_user_name = user_name[0]
    for i in range(1, len(user_name)-1):
        encoded_user_name += "*"
    return encoded_user_name+user_name[-1]+"@"+email_components[1]
    

if __name__ == "__main__":
    for mail in email:
        encoded_email = encode_email(mail)
        logger.info(f"Encoded email: {encoded_email}")