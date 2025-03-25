import sys


#My function "konverter" takes the different kinds of sizes and convert
#Into numbers for the rigth size

#Then it returns the rigth number for each type with the return "tall"
def konverter(verdi):

    tall, enhet = verdi.split()

    tall=float(tall)

    if "Kbps" in enhet :
        return tall * 1000
    if "Mbps" in enhet :
        return tall * 1000000
    if "Gbps" in enhet :
        return tall * 1000000000

    return tall

#The function "throughputs first sets a value N that should be the lengt og throughtput
#Then does the equation with the N instead og the length og throughputs
#And returns the result of the equation

def jfi(throughputs):
    N = len(throughputs)
    return sum(throughputs) ** 2 / (N * sum(x ** 2 for x in throughputs))


#The Main function takes the filename that it is going to take information from
#With a "filnavn" parameter and then it converts the values in the fil
#After it prints out with the "Jain fairness Indeksen er:"
def main(filnavn):
    with open(filnavn) as fil:
        throughputs = [konverter(linje.strip()) for linje in fil]
        print(f"Jain's Fairness Indeksen er : {jfi(throughputs):.4f}")


#Lastly a usage of the build in __name__ in python to connect it with main.
if __name__ == "__main__":
    main(sys.argv[1])



