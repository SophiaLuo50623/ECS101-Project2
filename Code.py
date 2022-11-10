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
    c1 = []
    c2 = []
    c3 = []
    averages = []

    cafeteria1 = random.normalvariate(10, 8)
    cafeteria2 = random.normalvariate(15, 6)
    cafeteria3 = random.normalvariate(12, 5)

    c1.append(cafeteria1)
    c2.append(cafeteria2)
    c3.append(cafeteria3)

    for x in range(297):
        r = random.random()
        if r < (e / 100):
            i = random.randint(1, 3)
            if i == 1:
                c1.append(random.normalvariate(10, 8))
                return c1
            elif i == 2:
                c2.append(random.normalvariate(15, 6))
                return c2
            else:
                c3.append(random.normalvariate(12, 5))
                return c3

        else:
            average = sum(c1) / len(c1)
            averages.append(average)
            average2 = sum(c2) / len(c2)
            averages.append(average2)
            average3 = sum(c3) / len(c3)
            averages.append(average3)

            best = max(averages)

            return average.index(best)






