import uuid

instance_number = int(input('How many EC2 instances would you like unique names for? '))
department = input('What is the name of your department? ')
 
print('\nYour unique EC2 instance names are listed below:\n ')

for i in range (instance_number):
       
       print(department + '-' + str(uuid.uuid4()))