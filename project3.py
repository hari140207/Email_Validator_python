email = 'hari@gmail.com'
email = email.strip()
valid = True
# Email cannot be empty
if email =='':
    print("Email cannot  be empty")
    valid = False
#email must contain '@' and '.'
if  not ("." in email and "@" in email):
    print("Email must contain . and @")
    valid = False
#email must contain only one '@' symbol
if   email.count("@") != 1:
    print("Email must contain only one @ symbol")
    valid = False
#email must end with .org, .net, .com
if  not email.endswith((".com",".org",".net")):
    print("email must end with .com , .org ,  .net ")
    valid = False
#email must not be longer than 254 characters
if len(email) > 254:
    print("email should be under 254 characters")
    valid = False
if  not (email[0].isalnum() and email [-1].isalnum()):
    print("Email must start and end with characters and digits")
    valid = False
if valid :
    print("Email is valid")