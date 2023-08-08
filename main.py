
input_list = ['Андрей 9', 'Василий 11', 'Роман 7', 'X Æ A-12 45', 'Иван Петров 3', 'Андрей 6', 'Роман 11']

hours_enum = dict() #Словарь в котором по ключу сохраняем список сходящих часов
result = dict() #Отедльный словарь, где по ключу сохраняем сумму часов


for index in range(len(input_list)):
    input_list[index] = input_list[index].split(' ')
    input_list[index] = [' '.join(input_list[index][:-1]), input_list[index][-1]]
    if input_list[index][0] in result.keys():
        result[input_list[index][0]] = result[input_list[index][0]] + int(input_list[index][1])
        hours_enum[input_list[index][0]] = hours_enum[input_list[index][0]] + ',' + str(input_list[index][1])
    else:
        result[input_list[index][0]] = int(input_list[index][1])
        hours_enum[input_list[index][0]] = str(input_list[index][1])

for key in result:
    print(key + ': ' + hours_enum[key] + '; sum:', result[key])


