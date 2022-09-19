#-----------print 1-20

#for value in range(1,21):
#    print(value)

#------------list 1-1,000,000 and then print it

million=list(range(1,1000001))
#for value in million:
#    print(value)

#-------------min, max, and sum the million list

#min_million=min(million)
#print(min_million)

print(sum(million))

#print(max(million))

#-------------list and print odd numbers from 1-20

odds=list(range(1,21,2))
for value in odds:
    print(value)




#-------------list and print multiples of 3 from 3-30

threes=list(range(3,31,3))
for value in threes:
    print(value)


#--------------list and print the first 10 cubes

cubes=[]
for value in range(1,11):
    cube=value**3
    cubes.append(cube)
for value in cubes:
    print(value)



#---------------use list comprehension to list the first 10 cubes

cubes=[value**3 for value in range(1,11)]
#print(cubes)