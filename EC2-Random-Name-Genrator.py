import uuid

#This line of code allows the user to input how many
#EC2 instances they want names for.
instance_number = int(input('How many EC2 instances would you like unique names for? '))

#This line of code allows the user to input their
#department name used in the unique name.
department = input('What is the name of your department? ')
 
print('\nYour unique EC2 instance names are listed below:\n ')

#This for loop generates random characters and numbers that 
#will be included in the unique name.
for i in range (instance_number):
     print(department + '-' + str(uuid.uuid4()))