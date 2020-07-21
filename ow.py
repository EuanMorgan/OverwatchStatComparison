import requests
import json
import time

the_boys = {"paps":"Pops-22982","euan":"PumpingLemma-21110","flaps":"UwU-21801","rowan":"Integration-21600",}

#click compare

def compare(ax,bx):


    a = requests.get("https://ow-api.com/v1/stats/pc/EU/{}/heroes/mercy".format(ax))
    parsedA = a.json()
    print(parsedA)
    aPretty = json.dumps((parsedA["competitiveStats"]["careerStats"]["mercy"]),indent=4,sort_keys=True)
    a = parsedA["competitiveStats"]["careerStats"]["mercy"]

    b = requests.get("https://ow-api.com/v1/stats/pc/EU/{}/heroes/mercy".format(bx))
    parsedB = b.json()
    bPretty = json.dumps((parsedB["competitiveStats"]["careerStats"]["mercy"]),indent=4,sort_keys=True)
    b = parsedB["competitiveStats"]["careerStats"]["mercy"]
    
    #print(aPretty)
    name1 = ax.split("-")[0]
    name2 = bx.split("-")[0]

    to_delete_a = []
    to_delete_b = []
    print(aPretty)
    print(bPretty)

            

    for hero in ["mercy"]:
        print("=========== HERO: {} ===========".format(hero))
        time.sleep(4)
        for x in ["assists","average","best","combat","game","heroSpecific"]:
            for (k,v) in parsedA["competitiveStats"]["careerStats"][hero][x].items():
                if k in parsedB["competitiveStats"]["careerStats"][hero][x]:

                    
                    print("---------------------------------------------------------------")
                    print(k)
                    v2 = parsedB["competitiveStats"]["careerStats"][hero][x][k]
                    time.sleep(0.3)
                    
                    print("{} {} \t {} {}".format(name1,v,name2,v2))
                    
                    try:
                        print("{} wins by {}".format(name1, v-v2) if v>v2 else "{} wins by {}".format(name2,v2-v))
                    except:
                        pass
                    time.sleep(4)
                    


    
    


x = input("Enter player one >>")
y = input("Enter player two >>")

compare(the_boys[x],the_boys[y])    