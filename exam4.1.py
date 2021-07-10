import random as rand
from random import random ,randint
import csv


#Task #1
def get_type(list_):
    dict_ = {}
    for i in list_:
        dict_[f'{type(i)}'] = i
    print(dict_)
    return dict_


lst_ = [1, 4.7, 'hi', False, None]
get_type(lst_)
#ничего более тупого я не придумал)
size_5 = f'''   *        *
               *   *   *   *
             *       *       *
           *                   *
         *                      *'''
size_6 =  f'''            *                     *
                      *       *             *       *
                  *               *      *              * 
              *                       *                     *
          *                                                     *
        *                                                          *'''

def printer():
    size = int(input())
    if size == 5:
        print(size_5)
    else:
        print(size_6)

printer()
#Task #3
lst1 = []
lst2 = []
lst3 = []
a = rand.randrange(0, 10)
for i in range(10):
    lst1.append(randint(0, 40))
    lst2.append(randint(0,40))
print(lst1,lst2)
for i in lst1:
    for j in lst2:
        if i == j:
            lst3.append(i)
print(lst3)

#task #4
def num_sum(a):
    suma = 0

    while a > 0:
        digit = a % 10
        suma = suma + digit
        a = a // 10

    print("Сумма:", suma)

num_sum(23423)

#Task #5 задание выполнено не до конца и коряво
class Reader:
    data = [['football_club', 'country', 'income', 'stadium'],
            ['Liverpool', 'England', '375000', 'Enfield'],
            ['FCB', 'Spain', '5000000', 'Camp-nou'],
            ['Juve', 'Italy', '46456550', 'Maracana'],
            ['RMA', 'Spain', '78099909', 'Santiago Bernabeu'],
            ['Man U', 'England', '567799', 'Old Trafford'],
            ['Man C', 'England', '7897007', 'Etihad Stadium'],
            ['Chelsea', 'England', '56777799', 'Stamford Bridge']]

    def writer(self):
        with open('sw_data_new.csv', 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            for row in self.data:
                writer.writerow(row)

        with open('sw_data_new.csv') as f:
            print(f.read())

    def sorter(self):
        with open('sw_data_new.csv', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=",")
            sortedlist = sorted(spamreader, key=lambda row: (row['football_club']), reverse=False)
        return sortedlist



r = Reader()
r.writer()
print(r.sorter())
