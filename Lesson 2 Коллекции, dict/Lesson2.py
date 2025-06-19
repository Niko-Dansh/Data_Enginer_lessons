list1 = list(   (1, 2, 4, '3','hello', None,bool(1), bool(0), bool, True, False)   )

# Use this block to prevent execution during import
if __name__ == "__main__":
    # This code will only run if this file is executed directly

     print(list1)
     #print(list1[1])

     print('-' * 200)

     list2 = list(   (type(1), type(2), type(4), type('3'),type('hello'), type(None), type(bool(1)), type(bool(0)), type(bool), type(True), type(False))   )
     print(list2)



     # Вывод с табуляцией
     for item1, item2 in zip(list1, list2):
          print(f"{item1}\t{item2}")

     list3 = list1 + list2

     print(list3)

     list4_unique = list(set(list3))

     print(list4_unique)

     list5_try = [1,1,2,2,3,3,4,4,5,5,6,6]
     list5_try_unique = list(set(list5_try))
     print(list5_try)
     print(set(list5_try))
     print(list5_try_unique)
