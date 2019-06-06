x1=input()
if((x1>='a')and(x1<='z'))or((x1>='A')and(x1<='Z')):
     if ((x1=='a')or( x1=='e')or(x1=='i')or(x1=='o')or(x1=='u')or(x1=='A')or(x1=='E')or(x1=='I')or(x1=='O')or(x1=='U')):
         print("Vowel")
     else:
         print("Consonant")
else:
    print("Invalid")
