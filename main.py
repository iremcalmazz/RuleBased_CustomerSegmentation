import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("data/persona.csv")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()


##unique source and price column variaables
#SORU-2 :  Kaç unique SOURCE vardır? Frekansları nedir?
print(df["SOURCE"].value_counts())
print(df["SOURCE"].unique())
print(df["SOURCE"].nunique())
#2 unique sources : ['android' 'ios']
#android    2974
#ios        2026
#Name: SOURCE, dtype: int64

#Soru 3: Kaç unique PRICE vardır?


#Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?


#Soru 5: Hangi ülkeden kaçar tane satış olmuş?


#Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?


#Soru 7: SOURCE türlerine göre satış sayıları nedir?


#Soru 8: Ülkelere göre PRICE ortalamaları nedir?


#Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?


#Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

#Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

l=["COUNTRY", "SOURCE", "SEX", "AGE"]
df.groupby(l).agg({"PRICE":"mean"})

#Görev 3: Çıktıyı PRICE’a göre sıralayınız.
#Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
#Çıktıyı agg_df olarak kaydediniz.
agg_df=df.groupby(l).agg({"PRICE":"mean"}).sort_values(by='PRICE', ascending=False)
agg_df.head()
#Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
agg_df = agg_df.reset_index()
agg_df.head()

#Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
agg_df.head()
print(agg_df["AGE"].max()) # AGE değişkenimizdeki maksimum yaşı bulduk.
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins=[0, 18, 23, 30, 40, 66],
                            labels=["0_18", "19_23", "24_30", "31_40", "41_66"])

#Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
agg_df["customers_level_based"] = [str(row[0]).upper() + "_" + str(row[1]).upper() +
                                    "_" + str(row[2]).upper() + "_" + str(row[5]).upper() for row in agg_df.values]
agg_df = agg_df[["customers_level_based","PRICE"]]

#Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
#(Segmentlere göre group by yapıp price mean, max, sum’larını alınız

agg_df.groupby(["SEGMENT"]).agg({"PRICE": ["min", "max", "mean"]})


#Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
#33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
#A
#35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
#C
def cat_summary(dataframe, col_name, plot=False):

    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

cat_summary(df, "SOURCE", plot=True)
cat_summary(df, "SEX", plot=True)


