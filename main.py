person={
    'name': 'Xaqani',
    'surname': 'Mirzeyev',
    'age': 21
}
print(person['surname'])

mounth = {
    '1': 'Yanvar',
    '2': 'Fevral',
    '3': 'Mart',
    '4': 'Aprel',
    '5': 'May',
    '6': 'Iyun',
    '7': 'Iyul',
    '8': 'Avqust',
    '9': 'Sentiyabr',
    '10': 'Oktyabr',
    '11': 'Noyabr',
    '12': 'Dekabr',
}

for i in range(13):
    mounth_number = input('Ayi daxil et: ')
    print(mounth_number, '-ci ay: ', mounth.get(mounth_number, 'Daxil edilen ay teyin olunmadi'))


# person = dict({
#     'name': 'Xaqani',
#     'surname': 'Mirzeyev',
#     'age': 21
# })
# print(person['surname'])


# class Car():
#     def __init__(self):
#         self.make = 'BMW'
#         self.model='X5'

# BMW=Car()

# print(BMW.model)