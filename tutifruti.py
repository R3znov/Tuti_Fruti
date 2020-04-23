import random
import os


arr = os.listdir()


var = input("Empezar: y / n \n")


while var != 'y' and var != 'n':
    print('Es "y" o "n" pelotudo no es muy dificil')

    var = input("Empezar: y / n \n")



while var == 'y':
        
    pregunta = input("Letra :   \n")

    for file in arr:

        if file.endswith(".txt"):

            letra = pregunta

            with open(file, 'r') as f:

                array = []
                
                for line in f:
                    
                    if line.startswith(letra.upper()):

                        array.append(line)


                if array:

                    total = len(array) - 1
                    
                    aleatorio = None

                    for x in range(1):
                        aleatorio = random.randint(0, total)

                    print (file[:-4] + " : " + array[aleatorio])

                

                else:
                    print ('no hay ' + file[:-4] + ' con ' + letra + ' \n')

    var = input("Seguir: y / n \n")

    


if  var == 'n':
    
    print("Nos Re Vimos")



        
    









    








