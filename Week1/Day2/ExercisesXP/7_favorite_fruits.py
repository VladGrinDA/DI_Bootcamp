fav_fruits_inp = input('Please enter your favorite fruits (seperate with space): ')
fav_fruits_list = fav_fruits_inp.split()

new_fruit_inp = input('Please input name of any fruit: ')

if new_fruit_inp in fav_fruits_inp:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')


