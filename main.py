def twosum(Numbers , Target):
    n = len(Numbers)
    for i in range(n):
        for j in range(i+1,n):
            if Numbers[i]+Numbers[j]==Target:
                print(f"[{i},{j}]")
                return i,j


twosum([2,4,6,7,9],9)