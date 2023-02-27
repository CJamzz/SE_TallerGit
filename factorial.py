 
def numero_factorial (N, F=1): 
                  
    if N != 0:

        for i in range (1, N+1):
            F = F * i

    print ("El factorial del número", N, "es", F)


numero_factorial(N =int(input("Dame un número: ")))
