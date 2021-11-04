usernames = ['david' , 'alice' , 'admin' , 'bob' , 'eric']

for user in usernames:
    if user == 'admin':
        print(f'hello {user}, would you like to see status report?')
    else:
        print(f'hello {user}, thank you for logging in again.')