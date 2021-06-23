# list supports =
list=[1,2,3]
list[0]="hari"
print(list)

#tuple does not support assignment =
tup=(1,2,3,4.6,"ram")
print(tup)
print(tup[4])
#tup[4]="raja"

# another form
tup1 = 1,2,3,4
print(tup1)

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
# Concatenating above two
print(tuple1 + tuple2)
tuple3=tuple1+tuple2
print(tuple3)
print("length is ",len(tuple3))


tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)
print(tuple3)

tuple1 = ('python', 'good')
tuple2 = (4,6,7,1,1.6,0.4)
print ('Maximum element in tuples 1 = ' +str(max(tuple1)))
print ('Maximum element in tuples 2 = ' +str(max(tuple2)))

print ('Minimum element in tuples 1 = ' +str(min(tuple1)))
print ('Minimum element in tuples 2 = ' +str(min(tuple2)))

lt=[34,56,2,1]
print(sorted(lt))
lt=sorted(lt)
print(lt)
#using sorted function after uddation it has become a list
lt1=(34,56,2,1)
print(sorted(lt1))
lt1=sorted(lt1)
print(lt1)

print(sum(lt1))







