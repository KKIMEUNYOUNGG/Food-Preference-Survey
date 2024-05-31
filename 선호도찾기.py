
# 3주 동안 먹은 음식의 종류와 점수
key=[
    [4.5,'일식','아침'], 
    [4.5,'중식','저녁'],
    [2,'한식','아침'],
    [4,'양식','저녁'],
    [4,'한식','아침'],
    [0.5,'중식','저녁'],
    [5,'한식','아침'],
    [2,'한식','저녁']

    ]

# 빈 리스트 만들기 (아침, 저녁)
list_breakfast=list()
list_dinner=list()

# 아침, 저녁으로 리스트 각각 저장하기
for item in key:
    if item[2]=='아침':
        list_breakfast.append(item)
    else:
        list_dinner.append(item)
        
# 잘 저장 되었는지 확인        
# print(list_breakfast)
# print(list_dinner)

# 빈 리스트 만들기 (한식, 중식, 일식, 양식)
breakfast_hansik=list()
breakfast_jungsik=list()
breakfast_illsik=list()
breakfast_yangsik=list()

# 아침에서 한, 중, 일, 양 나누기
for item in list_breakfast:
    if item[1]=='한식':
        breakfast_hansik.append(item)
    elif item[1]=='중식':
        breakfast_jungsik.append(item)
    elif item[1]=='일식':
        breakfast_illsik.append(item)
    else:
        breakfast_yangsik.append(item)
        
# 평균 계산 함수
def average(lst):
    if len(lst) == 0:
        return 0
    total = sum(item[0] for item in lst)
    return total / len(lst)

# 아침의 각 음식 종류의 평균 계산
average_breakfast_hansik = [f"{average(breakfast_hansik):.1f}", '한식', '아침']
average_breakfast_jungsik = [f"{average(breakfast_jungsik):.1f}", '중식', '아침']
average_breakfast_illsik = [f"{average(breakfast_illsik):.1f}", '일식', '아침']
average_breakfast_yangsik = [f"{average(breakfast_yangsik):.1f}", '양식', '아침']

# 잘 저장되었는지 확인
# print(average_breakfast_hansik)
# print(average_breakfast_jungsik)
# print(average_breakfast_illsik)
# print(average_breakfast_yangsik)

# 빈 리스트 만들기 (한식, 중식, 일식, 양식)
dinner_hansik=list()
dinner_jungsik=list()
dinner_illsik=list()
dinner_yangsik=list()

# 저녁에서 한, 중, 일, 양 나누기
for item in list_dinner:
    if item[1]=='한식':
        dinner_hansik.append(item)
    elif item[1]=='중식':
        dinner_jungsik.append(item)
    elif item[1]=='일식':
        dinner_illsik.append(item)
    else:
        dinner_yangsik.append(item)
        
# 저녁의 각 음식 종류의 평균 계산
average_dinner_hansik = [f"{average(dinner_hansik):.1f}", '한식', '저녁']
average_dinner_jungsik = [f"{average(dinner_jungsik):.1f}", '중식', '저녁']
average_dinner_illsik = [f"{average(dinner_illsik):.1f}", '일식', '저녁']
average_dinner_yangsik = [f"{average(dinner_yangsik):.1f}", '양식', '저녁']

# 잘 저장되었는지 확인
# print(average_dinner_hansik)
# print(average_dinner_jungsik)
# print(average_dinner_illsik)
# print(average_dinner_yangsik)

print(average_breakfast_hansik)
print(average_breakfast_jungsik)
print(average_breakfast_illsik)
print(average_breakfast_yangsik)
print('')
print(average_dinner_hansik)
print(average_dinner_jungsik)
print(average_dinner_illsik)
print(average_dinner_yangsik)
