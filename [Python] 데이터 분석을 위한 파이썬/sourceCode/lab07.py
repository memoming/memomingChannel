
# 포켓몬카운터 v2.0 :: 그래프 넣어보기

import matplotlib.pyplot as plt

def readTxt_returnList( txtPath ) :
    fStream = open(txtPath,encoding="utf-8")
    rltList = fStream.readlines()
    fStream.close()
    return rltList


dataFilePath    = "lab02_poketmon/poketmon_data.txt"
indexFilePath   = "lab02_poketmon/poketmon_index.txt"

# index 파일을 읽어서 포켓몬 이름이 들어가 있는 리스트만들기
poketmon_name_list = list()

# fStream = open(indexFilePath,encoding="utf-8")
# temp_list = fStream.readlines()
# fStream.close()

temp_list = readTxt_returnList(indexFilePath)
for i in temp_list :
    poketmon_name_list.append( i.strip() )


# 포켓몬 이름이 있는 리스트와 동일한 길이의 리스트를 만들고 0으로 초기화해두기
poketmon_count_list = list()

for i in poketmon_name_list :
    poketmon_count_list.append(0)

print(len(poketmon_name_list))
print(len(poketmon_count_list))


# Data 파일을 읽어서 반복문을 돌면서 해당 포켓몬이 들어있는 index 값 찾기
# fStream = open(dataFilePath,encoding="utf-8")
# all_poketmonData_list = fStream.readlines()
# fStream.close()

all_poketmonData_list = readTxt_returnList(dataFilePath)

for each in all_poketmonData_list :
    each_poketmon = each.strip()
    target_index = poketmon_name_list.index( each_poketmon )

    # 0으로 초기화 해두었던 list에 위에서 찾았던 index번호에 +1 해주기
    poketmon_count_list[target_index] += 1


print(poketmon_name_list)
print(poketmon_count_list)


# 이쁘게 출력하기
for i in range( len(poketmon_name_list) ) :
    print(poketmon_name_list[i], ":", poketmon_count_list[i])


# plt 한글문제 해결하기
def setKFont() :
    from matplotlib import font_manager, rc
    font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/HYBDAL.TTF").get_name()
    rc("font", family=font_name)
    plt.rcParams["font.size"] = 15
    plt.rcParams["figure.figsize"] = (14,8)



# 그래프 출력하기
setKFont()



plt.subplot(2,1,1)
plt.bar(poketmon_name_list,poketmon_count_list, width=0.5, color="grey")
plt.title("포켓몬 카운터 ver 2.0")
plt.xlabel("Poketmon name")
plt.ylabel("num of poketmon")

plt.subplot(2,1,2)
plt.plot(poketmon_name_list, poketmon_count_list)
plt.xlabel("Poketmon name")
plt.ylabel("num of poketmon")

plt.show()

