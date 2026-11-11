import re
def check_password_strength(password):
    if len(password)<10:
        return"Password too short!(Min 10 characters)"
    if len(re.findall(r"[A-Z]",password))<2:
        return"Add atleast two capital letters!"
    if not re.search(r"[0-9]",password):
        return"Add atleast one number!"
    if not re.search(r"[\-!@#$%^&*()_~`?/:;'<>|{}]",password): 
        return"Add atleast one special character!"
    return"Strong Password"
while True:
    user_input=input("Enter your password: ")
    result=check_password_strength(user_input)
    print(result)
    if result=="Strong Password":
        break
    
