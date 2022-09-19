#----if an alien's color is green and the player shot it down, award 5 points. Yellow, award 10 points. Red, 15 points.

alien_color='yellow'
if alien_color=='green':
    print(f'You shot a {alien_color} alien! Your score is 5\n')
elif alien_color=='yellow':
    print(f'You shot a {alien_color} alien! Your score is 10\n')
elif alien_color=='red':
    print(f'You shot a {alien_color} alien! Your score is 15\n')
else:
    print('')


#----Print stages of life. <2 years is baby. >=2 years but <4 is toddler. >=4 but <13 is kid. >=13 but <20 is teenager.
#----->=20 but <65 is adult. >=65 is elder.

age=90
if age<2:
    life_stage='baby'
elif age>=2 and age<4:
    life_stage='toddler'
elif age>=4 and age<13:
    life_stage='kid'
elif age>=13 and age<20:
    life_stage='teenager'
elif age>=20 and age<65:
    life_stage='adult'
elif age>=65:
    life_stage='dinosaur'

print(f'You are {age} years old? Your life stage is: {life_stage}!\n')

#----Make a list of three of your favorite fruits. Write 5 if statements. The output should include all matches.

favorite_fruits=['banana','kiwi','pineapple']
if 'banana' in favorite_fruits:
    print('Gotta have bananas!')
if 'strawberry' in favorite_fruits:
    print('Gotta have strawberries!')
if 'kiwi' in favorite_fruits:
    print('Gotta have kiwis!')
if 'orange' in favorite_fruits:
    print('Gotta have oranges!')
if 'pineapple' in favorite_fruits:
    print('Gotta have pineapples!')


