Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a, b, c = 1, 1, 1
>>> while c < 11 :
	print(b, end=" ")
	a, b, c = b, a+b, c+1

	
1 2 3 5 8 13 21 34 55 89 
>>> k = 1
>>> while k < 20:
	print(k*7, end=" ")
	k = k +1

	
7 14 21 28 35 42 49 56 63 70 77 84 91 98 105 112 119 126 133 
>>> 