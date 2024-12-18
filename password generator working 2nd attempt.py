user = input ('do want a random password to be generated, if so type yes:')



if user.lower() == 'yes':
    
   
    user_request = True

    while user_request:
        lens = input ('how long do you want it (max 1000 characters):')
        if str(lens).isdigit():
            lens = int(lens)
        
            if lens <= 1000 and lens>0:
                
                 print ('okay')
                 
                 print ('a password of',lens,'characters is coming right up')
         
                 password = ''
                 import string 
                 import random
                 for i in range(lens):
                     
                     password += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits+string.punctuation)
                 print ('here is ur',lens,'character password:')
                 print (password)
                 again = input('Want to go again?')
                 if again.lower() != 'yes':
                     print ('BYE!!')
                     user_request = False 
                 else :
                     print ('lets make another one!!')
                     continue
            else : 
                print ('length must be between 1 to 1000')
        else :
            print ('length has to be a number')
            
             
else :
    print ('y are u here then')
