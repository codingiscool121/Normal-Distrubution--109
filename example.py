import random
import plotly.figure_factory as pf
import plotly.express as pd
import statistics as st

dice=[]
count=[]
for i in range(0,100):
    count.append(i)
    dice1=random.randint(1,6)
    dice2 = random.randint(1,6)
    dice.append(dice1+dice2)
#if all three are same, normal distrubtion is perfect.
mean = st.mean(dice)
median = st.median(dice)
mode=st.mode(dice)
stand= st.stdev(dice)
#These are the ranges of the normal distrubtion.
firstsdstart,firstsdend = mean-stand, mean+stand
secondsdstart,secondsdend = mean-2*stand, mean+2*stand
thirdsdstart,thirdsdend = mean-3*stand, mean+3*stand
print(mean)
print(median)
print(mode)
print(stand)
print("First part of range(left): ", firstsdstart)
print("Last part of range(right)", firstsdend)

print("First part of range(left) second part: ", secondsdstart)
print("Last part of range(right) second part", secondsdend)

print("First part of range(left) third part: ", thirdsdstart)
print("Last part of range(right) third part", thirdsdend)

fd= [i for i in dice if firstsdstart<i<firstsdend]
print(fd)

sd = [i for i in dice if secondsdstart<i<secondsdend]
print(sd)

td = [i for i in dice if thirdsdstart<i<thirdsdend]
print(td)

#Region 1 %
fddata= len(fd)
length = len(dice)
fraction1 = (fddata/length)*100.0
print("Percentage for first region: ", fraction1)

sddata= len(sd)
length = len(dice)
fraction2 = (sddata/length)*100.0
print("Percentage for second region: ", fraction2)

tddata= len(td)
length = len(dice)
fraction3 = (tddata/length)*100.0
print("Percentage for third region: ", fraction3)
print("{}% of data in the third region".format(fraction3) )
graph=pd.bar(x=dice, y=count)
graph.show()
# Creating normal distrubution graph
graph1=pf.create_distplot([dice], ["Dice results"])
graph1.show()

