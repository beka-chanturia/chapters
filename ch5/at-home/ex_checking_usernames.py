current_users = ['alice' , 'bob' , 'liz' , 'zed' , 'david']
new_users = ['eli' , 'mike' , 'bob' , 'carla' , 'liz']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'The username "{new_user}" is not available, please choose other.')
    else:
        print(f'username {new_user} is available.')