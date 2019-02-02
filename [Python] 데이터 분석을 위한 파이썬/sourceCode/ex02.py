
# 실습예제 포켓몬 카운터 만들어보기

dataFilePath    = "lab02_poketmon/poketmon_data.txt"
indexFilePath   = "lab02_poketmon/poketmon_index.txt"

# index 파일을 읽어서 포켓몬 이름이 들어가 있는 리스트만들기
poketmon_name_list = list()

fStream = open(indexFilePath,encoding="utf-8")
temp_list = fStream.readlines()
for i in temp_list :
    poketmon_name_list.append( i.strip() )
fStream.close()


# 포켓몬 이름이 있는 리스트와 동일한 길이의 리스트를 만들고 0으로 초기화해두기
poketmon_count_list = list()

for i in poketmon_name_list :
    poketmon_count_list.append(0)

print(len(poketmon_name_list))
print(len(poketmon_count_list))


# Data 파일을 읽어서 반복문을 돌면서 해당 포켓몬이 들어있는 index 값 찾기
fStream = open(dataFilePath,encoding="utf-8")
all_poketmonData_list = fStream.readlines()
for each in all_poketmonData_list :
    each_poketmon = each.strip()
    target_index = poketmon_name_list.index( each_poketmon )

    # 0으로 초기화 해두었던 list에 위에서 찾았던 index번호에 +1 해주기
    poketmon_count_list[target_index] += 1
fStream.close()

print(poketmon_name_list)
print(poketmon_count_list)


# 이쁘게 출력하기
for i in range( len(poketmon_name_list) ) :
    print(poketmon_name_list[i], ":", poketmon_count_list[i])

