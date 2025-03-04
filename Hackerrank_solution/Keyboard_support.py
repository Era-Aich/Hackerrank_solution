

def keyboar(b,n,m,key_price,usb_pice):
    max_spent = -1
    for i in range(n):
        for j in range(m):
            total = key_price[i] + usb_pice[j]
            if total<=b:
                max_spent = max(max_spent, total)
    return max_spent



b,n,m = map(int,input().split())
key_price = list(map(int,input().strip().split()))
usb_pice = list(map(int,input().strip().split()))

result = keyboar(b, n, m, key_price, usb_pice)
print(result)