# spørg brugere en liste over 3 venner
# Nærste by på vennerne
# Gem i nearby friend

friends = input('Indtast 3 navne med komma imellem, dog uden mellemrum: ').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()] #strip fjerne alle mellemrum, linjeskift osv.

people.close()

friends_set = set(friends) #Fjerne dubletter
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set) #summerer de 2 set's

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} er nærmeste! Lad mig møde dem.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()