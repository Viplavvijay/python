s=input("enter a string ::")
c=0
print("enter the choice:\n1-To capitalize\n2-To convert in lower case\n3-to count character\n4-get encoded version\n5-to check whether it ends with particular value\n6-to find particular value\n7-to check if all characters are alphanumeric\n8-to check if all characters are alphabet\n9-to check if all characters are decimal\n 10-to check if all characters are digits\n11-to check if the string is an identifier\n12-to check if all the charcters are in lower case\n 13-to check if all the charaters are numeric\n14-to check if all the characters in the string are printable\n15-to check if all the characters are whitespaces\n 16-to check if the string follows the rule of title\n17-to check if the string is in upper case\n18-returns a left justifies string\n 19-to convert astring to lower case\n20-to get a left trimmed version of the string\n 21-to get a tuple where the string is divided into three parts\n22-to find the last position of a value\n 23-to find the last index of a value\n24-to get a right justified version of the string\n25-to get a right trim version of string\n 26-to split lines\n27-to get a trimmed version of the string\n28-to convert first letter to upper case of each word\n 29-to convert the string to upper case\n30-to get a translated string")

print("*****************************************")
print("##########################################")
while(1):
    c=int(input("enter choice::"))
    if c==1:
        print(s.capitalize())
    elif c==2:
        print(s.casefold())
    elif c==3:
        b=input("enter the char to count::")
        print(s.count(b))
    elif c==4:
        print(s.encode())
    elif c==5:
        print(s.endswith(" "))
    elif c==6:
        c=input("enter value to find::")
        print(s.find())
    elif c==7:
        print(s.isalnum())
    elif c==8:
        print(s.isalpha())
    elif c==9:
        print(s.isdecimal())
    elif c==10:
        print(s.isdigit())
    elif c==11:
        print(s.isidentifier())
    elif c==12:
        print(s.islower())
    elif c==13:
        print(s.isnumeric())
    elif c==14:
        print(s.isprintable())
    elif c==15:
        print(s.isspace())
    elif c==16:
        print(s.istitle())
    elif c==17:
        print(s.isupper())
    elif c==18:
        print(s.ljust())
    elif c==19:
        print(s.lower())
    elif c==20:
        print(s.lstrip())
    elif c==21:
        print(s.partition())
    elif c==22:
        d=input("enter value to find its last position::")
        print(s.rfind(d))
    elif c==23:
        e=input("enter value::")
        print(s.rindex(e))
    elif c==24:
        print(s.rjust())
    elif c==25:
        print(s.rstrip())
    elif c==26:
        print(s.splitlines())
    elif c==27:
        print(s.strip())
    elif c==28:
        print(s.title())
    elif c==29:
        print(s.upper())
    elif c==30:
        print(s.translate())
    elif c==31:
        break

    