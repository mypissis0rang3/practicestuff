def aura_time(time):
    time= time.lower()
    comaura=["internacional de porto alegre", "inter", "internacional"]

    if time in comaura:
        return "Com aura"
    else:
        return "Sem aura"
    
time= input("Diga o nome do time para calcular a aura:")
print(aura_time(time))