def distance_hamming(Premiermot,Deuxièmemot):
    index=0
    distance=0
    while index<len(Premiermot):
        if Premiermot[index]!=Deuxièmemot[index]:
            distance=distance+1
        index=index+1
    return(str(distance))
print(distance_hamming("japon","savon"))