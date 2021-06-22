class Solution:        
    def romanToInt(self, s: str) -> int:
        number = 0
        ultimo = True
        list_s = []
        for i in s:
            list_s.append(i)
        for i in range(len(list_s)-2):
            #print(i, number)
            if list_s[i] == "I":
                if list_s[i+1] == "V":
                    number += 4
                    list_s[i+1] = " "
                elif s[i+1] == "X":
                    number += 9
                    list_s[i+1] = " "
                else:
                    number += 1
            elif list_s[i] == "V":
                number += 5
            elif s[i] == "X":
                if list_s[i+1] == "L":
                    number += 40
                    list_s[i+1] = " "
                elif list_s[i+1] == "C":
                    number += 90
                    list_s[i+1] = " "
                else:
                    number += 10
            elif list_s[i] == "L":
                number += 50
            elif list_s[i] == "C":
                if list_s[i+1] == "D":
                    number += 400
                    list_s[i+1] = " "
                elif list_s[i+1] == "M":
                    number += 900
                    list_s[i+1] = " "
                else:
                    number += 100
            elif list_s[i] == "D":
                number += 500
            elif list_s[i] == "M":
                number += 1000
            #print("\t",i,number)
        #print("l-2",list_s[-2])
        #print("l-1",list_s[-1])
        if len(list_s) > 1:
            if list_s[-2] == "I":
                if list_s[-1] == "V":
                    number += 4
                    ultimo = False
                elif list_s[-1] == "X":
                    number += 9
                    ultimo = False
                else:
                    number += 1
            elif list_s[-2] == "X":
                if list_s[-1] == "L":
                    number += 40
                    ultimo = False
                elif list_s[-1] == "C":
                    number += 90
                    ultimo = False
                else:
                    number += 10
            elif list_s[-2] == "C":
                if list_s[-1] == "D":
                    number += 400
                    ultimo = False
                elif list_s[-1] == "M":
                    number += 900
                    ultimo = False
                else:
                    number += 100
            elif list_s[-2] == "V":
                number += 5
                ultimo = True
            elif list_s[-2] == "L":
                number += 50
                ultimo = True
            elif list_s[-2] == "D":
                number += 500
                ultimo = True
            elif list_s[-2] == "M":
                number += 1000
                ultimo = True
        #print(ultimo)
        if ultimo == True:
            if list_s[-1] == "I":
                number += 1
            elif list_s[-1] == "V":
                number += 5
            elif list_s[-1] == "X":
                number += 10
            elif list_s[-1] == "L":
                number += 50
            elif list_s[-1] == "C":
                number += 100
            elif list_s[-1] == "D":
                number += 500
            elif list_s[-1] == "M":
                number += 1000
        return number