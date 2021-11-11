age = 2

if age >= 18:
    print('you can vote')

if age < 4:
    ticket_price = 0
    print('ticket is free')

elif age < 18:
    ticket_price = 10
    print('ticket price is $10')

else:
    ticket_price = 15
    print('ticket price is $15')