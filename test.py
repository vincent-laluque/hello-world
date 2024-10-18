euroToDollar = 1.49
euro = 1
somme = 0
while somme < 16384:
    somme = euro*euroToDollar
    print(euro, " euro(s) = ", somme, " dollar(s)")
    euro = euro*2
    
   
u, n = 1, 1
while n <= 12:
    print(u, end=" ")
    u, n = u*3, n + 1
