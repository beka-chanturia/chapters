available_toppings = ['mushrooms' , 'olives' , 'green peppers' , 
                      'pepperoni' , 'pinapple' , 'extra cheese']

requested_toppings = ['mushrooms' , 'french fires' , 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('adding ' + requested_topping + '.')
    else:
        print('sorry we don\'t have ' + requested_topping + '.')

print('\nFinished making your pizza!')