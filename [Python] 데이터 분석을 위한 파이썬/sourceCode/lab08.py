import pandas as pd
import matplotlib.pyplot as plt

# 기본적인 Series와 DataFrame 출력해보기
# num_series = pd.Series([1,2,3,4,5], index=["index_0","index_1","index_2","index_3","index_4",])
# num_df = pd.DataFrame([1,2,3,4,5], index=["index_0","index_1","index_2","index_3","index_4",])

# print(num_series)
# print(num_df)


# pandas로 csv 파일 읽기

titanic_df = pd.read_csv("lab04_titanic/train.csv")

# print(titanic_df)
# print(titanic_df.info())

# 생존자와 비생존자를 카운트 해보기

alive = titanic_df[ titanic_df["Survived"] == 1 ]
dead  = titanic_df[ titanic_df["Survived"] == 0 ]

# print(len(alive) , "/" , len(titanic_df))
# print(len(dead) , "/" , len(titanic_df))

# plt.bar(["alive","dead"], height=[len(alive), len(dead)])
# plt.show()

# Scatter 이용해서 요금별 탑승자 시각화 하기
# plt.scatter(titanic_df["PassengerId"], titanic_df["Fare"])
# plt.xlabel("PassengerID")
# plt.ylabel("Fare")
# plt.show()

# 각각을 색상분류 후 시각화 해보기
# plt.scatter(alive["PassengerId"], alive["Fare"], color="GREEN")
# plt.scatter(dead["PassengerId"], dead["Fare"], color="RED")
# plt.xlabel("PassengerID")
# plt.ylabel("Fare")
# plt.show()

# $50 기준 탑승자 수 구해보기
over_50     = titanic_df[ titanic_df["Fare"] >= 50 ]
under_50    = titanic_df[ titanic_df["Fare"] < 50 ]

# print( len(over_50), "/", len(titanic_df),  str(len(over_50)/len(titanic_df)*100)[:5]+"%" )
# print( len(under_50), "/", len(titanic_df), str(len(under_50)/len(titanic_df)*100)[:5]+"%" )

# 생존자를 $50 기준으로 나눠보기
alive_over_50   = over_50[ over_50["Survived"] == 1 ]
alive_under_50  = under_50[ under_50["Survived"] == 1 ]

print(len(alive_over_50),"/",len(over_50),      str(len(alive_over_50)/len(over_50)*100)[:5])
print(len(alive_under_50),"/",len(under_50),    str(len(alive_under_50)/len(under_50)*100)[:5])


# pie chart로 나타내보기

# chart 1 : 50$ 미만에서 생존자와 비생존자 구분하기
plt.subplot(2,1,1)
plt.pie([len(alive_under_50),len(under_50)-len(alive_under_50)])

# chart 2 : 50$ 이상에서 생존자와 비생존자 구분하기
plt.subplot(2,1,2)
plt.pie([len(alive_over_50), len(over_50)-len(alive_over_50)])

plt.show()