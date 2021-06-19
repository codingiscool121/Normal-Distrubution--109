import pandas as pd
import statistics as st

data=pd.read_csv("heightweight.csv")
height = data["Height"].tolist()
hmean = st.mean(height)
hsd = st.stdev(height)

fdstart, fdend = hmean-hsd, hmean+hsd
sdstart, sdend = hmean-2*hsd, hmean+2*hsd
tdstart, tdend = hmean-3*hsd, hmean+3*hsd

fdlist = [i for i  in height if fdstart<i<fdend]
sdlist = [i for i  in height if sdstart<i<sdend]
tdlist = [i for i  in height if tdstart<i<tdend]

print("{} of data within first region".format((len(fdlist)/len(height))*100.0))
print("{} of data within second region".format((len(sdlist)/len(height))*100.0))
print("{} of data within third region".format((len(tdlist)/len(height))*100.0))
