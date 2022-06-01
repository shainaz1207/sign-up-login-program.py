print('------Signup for creating an Account------')
usr=input('Enter Username: ')
pwd=input('Enter Password: ')
print('Your account have been created succesfully....!')
print("Login Now!")
name=input('Enter Username: ')
psw=input('Enter Password: ')
if(usr==name and psw==pwd):
    print('You have Logged in Succesfully!')
else:
    print('Invalid Details')
