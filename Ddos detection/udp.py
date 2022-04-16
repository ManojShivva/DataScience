import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./revised_kddcup_dataset.csv",index_col=0)
df.head()
udp_df = df[df.loc[:,"protocol_type"] == "udp"]
udp_df.to_csv("udp_attack.csv")
udp_df.head()
service_values = np.unique(udp_df.loc[:,"service"])
mid = (len(service_values)+1)/2
for i in range(len(service_values)):
    udp_df = udp_df.replace(service_values[i], (i-mid)/10)
udp_df.head()
features = ["service","src_bytes","dst_bytes","wrong_fragment","count","num_compromised","srv_count","dst_host_srv_count","dst_host_diff_srv_rate"]
target = "result"
X = udp_df.loc[:,features]
y = udp_df.loc[:,target]
classes = np.unique(y)
print(classes)
for i in range(len(classes)):
    if i == 1:
        udp_df = udp_df.replace(classes[i], 0)
    else:
        udp_df = udp_df.replace(classes[i], 1)

#turning the service attribute to categorical values
udp_df=udp_df.replace("eco_i",-0.1)
udp_df=udp_df.replace("ecr_i",0.0)
udp_df=udp_df.replace("tim_i",0.1)
udp_df=udp_df.replace("urp_i",0.2)
udp_df.head()
sns.heatmap(X.corr(), annot=True,cmap="RdBu")
plt.plot()
from sklearn.ensemble import RandomForestClassifier
y = udp_df.loc[:,target]