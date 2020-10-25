import random

print("Author: Jonathan Lin")
print("")
print("Adjusted to published proportions of age distributions")
print("Also adjusted for age expectancy differences between genders")
print("")
#0-4.9, 5-9.9, ... 75-79, 80+
#female distribution is just a few years older than males
male_dist = [2,1,1,1,2,2,2,2,3,3,3,5,6,8,12,13,16,39]
female_dist = [2,1,1,1,2,2,2,2,3,3,3,5,6,8,12,13,16,39]

#couldnt' figure out how to do weighted probability so this is my best solution lol
male_dist_prob = []
age = 0
for number in male_dist:
  for i in range(number):
    male_dist_prob.append(age)
  age = age + 5

female_dist_prob = []
age = 0
for number in female_dist:
  for i in range(number):
    female_dist_prob.append(age)
  age = age + 5

#create the actual numbers from the weighted distributions
male_out = []
for i in range(100):
  age = random.choice(male_dist_prob)
  age = age + random.randrange(1,5)
  male_out.append(age)

female_out = []
for i in range(100):
  age = random.choice(male_dist_prob)
  age = age + random.randrange(1,5)
  female_out.append(age)

female_out_edited = []
for number in female_out:
  female_out_edited.append(number + random.randrange(1,5)) #add 1-5 years because women tend to live longer


#convert output lists to numbers separated by spaces for easier copying and pasting
string = str(male_out).strip('[]')
print("Males: ")
while string.find(",") > -1:
  string = string[0:string.find(",")] + string[string.find(",")+1:len(string)]
print(string)
print("")
print("Females: ")
string = str(female_out_edited).strip('[]')
while string.find(",") > -1:
  string = string[0:string.find(",")] + string[string.find(",")+1:len(string)]
print(string)

print("")
print("")

print("If you are using the https://Age-Generator.jonathanlin04.repl.run link to run this code, refresh the page or press the \"run again\" button at the bottom to generate a new data set.")