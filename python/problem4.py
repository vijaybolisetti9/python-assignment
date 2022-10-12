#in this challenge man is asking to count the no of legs of the animals he mentiones while chicken have two ans cow have four and pig has four
# while the order is(hens,chickens ,pigs)


def animals(hens,cows,pigs):
    count_of_legs=0
    chickens_leg_count=int(hens)*2
    cows_leg_count=int(cows)*4
    pigs_leg_count=int(pigs)*4

    count_of_legs+=(chickens_leg_count+cows_leg_count+pigs_leg_count)
    return (count_of_legs)


list_of_animals=input().split()
hens,cows,pigs=list_of_animals
count_of_legs=animals(hens,cows,pigs)
print(count_of_legs)