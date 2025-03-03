
def maximum(n1, n2, n3):
    "renvoie le plus grand des trois nombres passés en argument"
    max = n1
    if (max < n2):
        max = n2
    if (max < n3):
        max = n3
    return max

print(maximum(2,5,4))
print(maximum(4.5, 5.7, 3.9))
print(maximum(8.2, 2.1, 6.7))
print(maximum(1.3, 4.8, 7.6))

