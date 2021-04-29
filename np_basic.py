import numpy as np

a = [1, 2, 3]
#print(a*3)

b = np.array(a)
#print(b*3)

#a = list(range(10000000))

def test():
    for i in range(len(a)):
        a[i] += 1

#%time test()

#%time [n+1 for n in range(10000000)]   # 754ms 리스트 컴프리헨션이 0.2초 더 빠름

b = np.arange(10000000)
#%time b+1     # 13ms 진짜빠름!

nd = np.array([1, 2, 3, 4, 5, 6, 7, 8])
nd2 = nd.reshape(4, 2)
#print(nd)
#print(nd2.reshape(1,-1))  #하나에 맞춰서 결정해줘 : -1  , matrix
#print(nd2.ravel())   # vector

# numpy와 list 다른점 : slicing
a = np.array([1, 2, 3, 4, 5])
b = a[:2]  # view
b[0] = 10
#print(a, b)  # slicing 원본과 연결 상태 . 값을 본다가 아니고 a의 0, 1번만 본다  = view

a = np.array([1, 2, 3, 4, 5])
b = a[0:2].copy()  # view 아닌 copy
b[0] = 10

# indexing
c = a[[0, 2]]         # 정수 인덱싱 : a[[row1, row2], [colu1, colu2]]
bul = a[[True, False, True, True, False]]   # boolean 인덱싱 : a[[True, false], [True, False...]]
#print(a, b)
#print(c)
#print(bul)  

c = a[a > 2]  # Fancy indexing !!!
#print(c)



# 연산
a = np.array([[1, 2], [3, 4]])
c = np.sum(a)  # sum : 배열 요소 모두 합침
print(c)
c = np.sum(a, axis=0)   #  열을 더해서 행으로 반환
print(c)
c = np.sum(a, axis=1)   #  행을 더해서 행으로 반환
print(d)

c = a[a > 2].sum()   # 2보다 큰 3, 4 구하여 더함
print(c)

 



