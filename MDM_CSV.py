import pandas as pd
import numpy as np
import missingno as msno
from matplotlib import pyplot as plt
from scipy import stats
from pprint import pprint
import seaborn as sns
import warnings

data = pd.read_csv("/Users/chichizhu/Desktop/xiaozhu_final.csv", encoding="gbk")
# print(data.shape) data lines and columns
#
# print(data.head(3)) first three lines

# print(data.info) whole sturcutre


# msno.matrix(data, figsize=(50, 50))
# plt.show()
'''To draw the data: full black in column means the data does not missing
white area represents the missing data
Conclusion: The rate part of the area have missing data'''


bj_sum = sum(data["city"] == "BJ")
sh_sum = sum(data["city"] == "SH")
gz_sum = sum(data["city"] == "GZ")
sz_sum = sum(data["city"] == "SZ")
cs_sum = sum(data["city"] == "CS")
wh_sum = sum(data["city"] == "WH")
cd_sum = sum(data["city"] == "CD")
cq_sum = sum(data["city"] == "CQ")

df = {
    "BeiJing": bj_sum, "ShangHai": sh_sum, "GuangZhou": gz_sum, "ShenZhen": sz_sum,
     "ChangSha": cs_sum, "WuHan": wh_sum, "ChengDu": cd_sum, "ChongQing": cq_sum,
}
# pprint(df)
# print out the total number for each city

bj_missing = sum(np.isnan(data.loc[data["city"] == "BJ", "rate"]))
sh_missing = sum(np.isnan(data.loc[data["city"] == "SH", "rate"]))
gz_missing = sum(np.isnan(data.loc[data["city"] == "GZ", "rate"]))
sz_missing = sum(np.isnan(data.loc[data["city"] == "SZ", "rate"]))
cs_missing = sum(np.isnan(data.loc[data["city"] == "CS", "rate"]))
wh_missing = sum(np.isnan(data.loc[data["city"] == "WH", "rate"]))
cd_missing = sum(np.isnan(data.loc[data["city"] == "CD", "rate"]))
cq_missing = sum(np.isnan(data.loc[data["city"] == "CQ", "rate"]))

'''Show missing value in bar graph for each city'''
# df = pd.DataFrame({
#         "city": ["BJ", "SH", "GZ", "SZ", "CS", "WH","CD", "CQ"],
#         "missing": [bj_missing, sh_missing, gz_missing, sz_missing, cs_missing, wh_missing, cd_missing, cq_missing],
#     })
# df = df.sort_values(by="missing", ascending=False)
# fig,ax = plt.subplots()
# fig.set_size_inches(12, 6)
# sns.barplot(data=df, x="city", y="missing", ax=ax)
# ax.set(xlabel="City", ylabel="Missing_Value", title="Each City Rate Missing Number")
# plt.rcParams["font.family"]="STSong"
# plt.tight_layout()
# plt.show()

print(data.head(2))
# For Whisker Box:

# fig, axes = plt.subplots()
# fig.set_size_inches(15, 10)

# sns.boxplot(y="rent_cost_day", data=data, orient="v", ax=axes[1][0])
# axes[1][0].set(ylabel="rent", title="Whiskerbox for rent")

# sns.boxplot(x="sex_landlord", y="rent_cost_day", data=data,orient="v")
# axes.set(ylabel="rent", xlabel="gender", title="Whiskerbox for different gender and rent")

# sns.boxplot(x="sumpeople", y="rent_cost_day", data=data,orient="v",ax=axes[1][0])
# axes[1][0].set(ylabel="Rent", xlabel="sumpeople", title="Whiskerbox for rent and people")
#
# sns.boxplot(x="beds", y="rent_cost_day", data=data,orient="v",ax=axes[1][1])
# axes[1][1].set(ylabel="rent", xlabel="bed", title="Whiskerbox for rent and bed")

# plt.tight_layout()
# plt.show()

# Mean and Standrad Deviation for Rent
# clean_data = data[np.abs(data["rent_cost_day"]-data["rent_cost_day"].mean()) <= (3*data["rent_cost_day"].std())]
# rent_mean=np.abs(data['rent_cost_day'].mean())
# print(rent_mean)
# rent_sd=np.abs(data['rent_cost_day'].std())
# print(rent_sd)



'''
Male and female review in number and diagram
'''
# data=data.dropna() # wash out all nan data for rate
# # print(data.head(30))
# # female_rate= data.loc[data['sex_landlord']== 'Female','rate']
# female_data=data[(data['sex_landlord']=='Female')]
# female_rate=female_data['rate']
# # print(female_rate)
# a=sum(female_rate)
# b=female_data.shape[0]
#
# print(a,b)
# female_avg=a/b
# print(female_avg)
# female_data.to_csv('female.csv')
# female_rate=data['rate']
# print(female_data)
# print(female_rate)


# data=data.dropna() # wash out all nan data for rate
# print(data.head(30))
# female_rate= data.loc[data['sex_landlord']== 'Female','rate']
# male_data=data[(data['sex_landlord']=='Male')]
# male_rate=male_data['rate']
# # print(female_rate)
# a=sum(male_rate)
# b=male_data.shape[0]
#
# print(a,b)
# male_avg=a/b
# print(male_avg)

'''
Rent per person for each gender
'''
#
# female_price= data.loc[data['sex_landlord']== 'Female','rent_cost_day']
#
# a=(sum(female_price)/female_price.shape[0])
#
# male_price= data.loc[data['sex_landlord']== 'Male','rent_cost_day']
#
# b=(sum(male_price)/male_price.shape[0])
# print(b,a)
# plt.figure(figsize=(6,9)) #调节图形大小
# labels = ['Male','Female']
# sizes = [b,a] #每块值
# colors = ['lightskyblue','yellow'] #每块颜色定义
# explode = (0,0) #将某一块分割出来，值越大分割出的间隙越大
# patches,text1,text2 = plt.pie(sizes,
#                       explode=explode,
#                       labels=labels,
#                       colors=colors,
#                       autopct = '%3.2f%%', #数值保留固定小数位
#                       shadow = False, #无阴影设置
#                       startangle =90, #逆时针起始角度设置
#                       pctdistance = 0.6) #数值距圆心半径倍数距离
# #patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
# # x，y轴刻度设置一致，保证饼图为圆形
# plt.axis('equal')
# plt.show()


