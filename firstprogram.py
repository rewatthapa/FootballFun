result1 = '' #print (*Team1, sep = ', ')
result2 = ''
result3 = ''

print ("Champions League First Semi Final")

#class championsleaguesemifinal1:
print ("Enter the goals scored by Liverpool")
LiverpoolScore = input()
print ("Enter the goals scored by AsRoma")
AsRomaScore = input()  
#def final1(FirstTeam):  
if LiverpoolScore > AsRomaScore:
  result1 = "Liverpool"
else:
  result1 = "AsRome"
#print (Final1)
#CLsemi1 = championsleaguesemifinal1()

print ("Champions League Second Semi Final")

#class championsleaguesemifinal2:
RealMadridScore = input ("Enter the goals scored by RealMadrid")
BayernMunichScore = input ("Enter the goals scored by BayernMunich")

if RealMadridScore > BayernMunichScore:
  result2 = ("Real MADRID")
else:
  result2 = ("Bayern Munich")
    
#CLsemi2 = championsleaguesemifinal2()
print ("The champions league final is between" + result1 + "  vs  " + result2)

Liverpool_Score = input ("Enter the goal scored by:" + result1)
RealMadrid_Score = input ("Enter the goal scored by:" + result2)

if Liverpool_Score > RealMadrid_Score:
  result3 = "The winner is LiverpoolFC"
else:
  result1 = "The winner are Motherfuckers"