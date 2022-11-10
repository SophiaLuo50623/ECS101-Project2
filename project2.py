import random


# Optimum happiness is 3000

def exploitOnly():
    happiness = 0
    cafeterias = []

    cafeteria1 = random.normalvariate(10, 8)
    cafeterias.append(cafeteria1)

    happiness += random.normalvariate(10, 8)

    cafeteria2 = random.normalvariate(15, 6)
    cafeterias.append(cafeteria2)

    happiness += cafeteria2

    cafeteria3 = random.normalvariate(12, 5)
    cafeterias.append(cafeteria3)

    happiness += cafeteria3

    best = max(cafeterias)

    if best == cafeteria1:
        for x in range(297):
            happiness += random.normalvariate(10, 8)

    elif best == cafeteria2:
        for x in range(297):
            happiness += random.normalvariate(15, 6)

    else:
        for x in range(297):
            happiness += random.normalvariate(12, 5)

    print(happiness)

def exploreOnly():
    happiness = 0
    for x in range(100):
        happiness += random.normalvariate(10, 8)
        happiness += random.normalvariate(15, 6)
        happiness += random.normalvariate(12, 5)

    # return happiness
    print(happiness)

def eGreedy(e = 10):
    averages = []
    cafeteria1 = [random.normalvariate(10, 8)]
    cafeteria2 = [random.normalvariate(15, 6)]
    cafeteria3 = [random.normalvariate(12, 5)]

    for x in range(297):
        r = random.random()
        if r < (e / 100):
            i = random.randint(1, 3)
            if i == 1:
                cafeteria1.append(random.normalvariate(10, 8))
            elif i == 2:
                cafeteria2.append(random.normalvariate(15, 6))
            else:
                cafeteria3.append(random.normalvariate(12, 5))

        else:
            average = sum(cafeteria1) / len(cafeteria1)
            averages.append(average)
            average2 = sum(cafeteria2) / len(cafeteria2)
            averages.append(average2)
            average3 = sum(cafeteria3) / len(cafeteria3)
            averages.append(average3)

            best_so_far = max(averages)

    return sum(cafeteria1) + sum(cafeteria2) + sum(cafeteria3) + best_so_far

result = eGreedy()
print(result)

def simulation(t,e):
    thappiness_exploit=0
    thappiness_explore=0
    thappiness_egreedy=0
    for i in range (t):
        thappiness_exploit+=exploitOnly()
        thappiness_explore+=exploreOnly()
        thappiness_egreedy+=eGreedy()
    a_exploit=thappiness_exploit/t
    a_explore=thappiness_explore/t
    a_greedy=thappiness_egreedy/t

    expected_explore=100*10+100*15*100*12
    expected_exploit=10+15+12+297*15
    expected_greedy=e*10+e*15+e*12+300*((100-e)/100)*15

    ehappy_c1=random.normalvariate(10,8)
    ehappy_c2=random.normalvariate(15,6)
    ehappy_c3=random.normalvariate(12,5)

    opt_happiness=300*15
    print("optimum happiness:",opt_happiness)
    print()

    print("Explore Only")
    print("Expected:%d" %expected_explore,"\t Regret: %d"%(opt_happiness-expected_exploit))
    print("Average: %d" %a_explore*"\t Regret: %d"%(opt_happiness-a_explore))
    print()

    print("Exploit Only")
    print("Expected: %d" %expected_exploit, "\t Regret: %d"%(opt_happiness-expected_exploit))
    print("Average: %d" %a_exploit,"\t Regret: %d"%(opt_happiness-a_exploit))

    print()
    print("eGreedy")
    print("Expected:%d"%expected_greedy,"\t Regret: %d"%(opt_happiness-expected_greedy))
    print("Average: %d" %a_greedy,"\t Regret: %d" %(opt_happiness-a_greedy))

    print()