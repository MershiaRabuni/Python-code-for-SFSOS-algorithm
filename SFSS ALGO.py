from pprint import pprint
import numpy as np

print("Step-1")
print("Enter the collection of Spherical fuzzy Soft Sets")
m = int(input("Number of Primary Spherical fuzzy Soft Sets: "))
rows = int(input("Enter the Number of attributes : "))
columns = int(input("Enter the Number of elements in the Universe Set: "))

SFS_Sets = []
a = [[0] * columns for i in range(rows)]
for i in range(m):
    print("Enter the Primary Spherical fuzzy soft set:", i + 1)
    sfs_set = [[tuple(map(float, input().split(" "))) for c in range(columns)] for r in range(rows)]
    SFS_Sets.append(sfs_set)

def sfs_compl(m):
    result = [[((m[r][c][2]), (m[r][c][1]), (m[r][c][0])) for c in range(columns)] for r in range(rows)]
    return (result)

def sfs_union(m1, m2):
    if [[(pow(max(m1[r][c][0], m2[r][c][0]),2), pow(max(m1[r][c][1], m2[r][c][1]),2),pow(min(m1[r][c][2], m2[r][c][2]),2)<=1)for c in range(columns)] for r in range(rows)]:
        result = [[((max(m1[r][c][0], m2[r][c][0])), (max(m1[r][c][1], m2[r][c][1])), (min(m1[r][c][2], m2[r][c][2]))) for c in range(columns)] for r in range(rows)]
        return(result)
    else:
        result = [[((max(m1[r][c][0], m2[r][c][0])), (min(m1[r][c][1], m2[r][c][1])), (min(m1[r][c][2], m2[r][c][2]))) for c in range(columns)] for r in range(rows)]
        return (result)
    
def sfs_int(m1, m2):
    result = [[((min(m1[r][c][0], m2[r][c][0])), (min(m1[r][c][1], m2[r][c][1])), (max(m1[r][c][2], m2[r][c][2]))) for c in range(columns)] for r in range(rows)]
    return (result)

def subset(m, A):
    if (m[i][j][0] == 1):
        return(((m[i][j][0] <= A[i][j][0]) and (m[i][j][1] >= A[i][j][1]) and (m[i][j][2] >= A[i][j][2])))
    else:
        return(((m[i][j][0] <= A[i][j][0]) and (m[i][j][1] <= A[i][j][1]) and (m[i][j][2] >= A[i][j][2])))
             

def superset(m, A):
    if (m[i][j][0] == 1):
        return True
    else:
        return(((m[i][j][0] >= A[i][j][0]) and (m[i][j][1] <= A[i][j][1]) and (m[i][j][2] <= A[i][j][2])))

def equal(A, m):
    return(((m[i][j][0] == A[i][j][0]) and (m[i][j][1] == A[i][j][1]) and (m[i][j][2] == A[i][j][2])))

Union = []
for m1 in SFS_Sets:
    for m2 in SFS_Sets:
        x1 = sfs_union(m1, m2)
        Union.append(x1)

Intersection = []
for m1 in SFS_Sets:
    for m2 in SFS_Sets:
        x2 = sfs_int(m1, m2)
        Intersection.append(x2)

Topology = []
for m1 in Union:
    for m2 in Intersection:
        if (np.array_equal(m1, m2) == False):
            Topology.append(m1)
            Topology.append(m2)

topology = []
for m1 in Topology:
    for m2 in Topology:
        if (np.array_equal(m1, m2) == False):
            y1 = sfs_union(m1, m2)
            y2 = sfs_int(m1, m2)
            topology.append(y1)
            topology.append(y2)

for m in Topology :
    topology.append(m)

res = [topology[i] for i in range(len(topology)) if i == topology.index(topology[i]) ]

print("Enter the absolute Spherical fuzzy soft point:")
l = [[tuple(map(float, input().split(" "))) for c in range(columns)]for r in range(rows)]

print("Step -2")
print("Frame the Spherical fuzzy Soft Topological Space")
res.append(l)
pprint (res)

complement = []
for m in res:
    x = sfs_compl(m)
    complement.append(x)

row = 1
col = 4
print("Step - 3")
print("Define a Suitable Operation")
A = [[tuple(map(float, input().split(" "))) for c in range(col)]for r in range(row)]

def operation(m):
    return (A[0][j][0] >= m[4][j][0] and A[0][j][1] >= m[4][j][1] and A[0][j][2] <= m[4][j][2])

ngamma = []
gamma = []
for m in res:
    mat = []
    for j in range(col):
        v = operation(m)
        mat.append(v)
    if all(mat):
        gamma.append(m)
    else:
        ngamma.append(m)


pprint(gamma)

print("Step-4")
print("Determine the Spherical fuzzy Soft Gamma Open Sets")
print("The Spherical fuzzy Soft Gamma Open Sets are:")

pprint(ngamma)

print("Seggregate the Spherical fuzzy Soft Gamma Open Sets")

seg = []
for l in range(len(SFS_Sets)):
    for k in range(len(ngamma)):
        cal2 = []
        for i in range(rows):
            for j in range(columns):
                v = equal(SFS_Sets[l],ngamma[k])
                cal2.append(v)
        if all(cal2):
            seg.append(SFS_Sets[l])

pprint(seg)

print("Step-5")
print("Determine the Union of Spherical fuzzy Soft Gamma Open Sets")

Uni = seg[0]
for g in range(len(seg)):
    Uni = sfs_union(Uni, seg[g])

pprint(Uni)

def transpose(A):
    res = []

    for col in range(len(A[0])):
        tmp = []
        for row in range(len(A)):
            tmp.append(A[row][col])

        res.append(tmp)

    return res

mat = transpose(Uni)

def comparision(a):
    l0 = []
    for i in range(columns):
        l1 = []
        for j in range(rows):
            m0 = 0
            m1 = 0
            m2 = 0
            for k in range(columns):
                if a[i][j][0] == 0 and a[i][j][1] == 0 and a[i][j][2] == 1:
                    m = 0
                else:
                    if a[i][j][0] >= a[k][j][0]:
                        m0 +=1
                    if a[i][j][1] >= a[k][j][1]:
                        m1 +=1
                    if a[i][j][2] >= a[k][j][2]:
                        m2 +=1
                    m = m0 + m1 - m2 - 1
            l1.append(m)
        l0.append(l1)
    return np.array(l0)

def score(a):
    return np.sum(comparision(a),axis=1)

def Output(a):
    return np.argmax(np.sum(comparision(a),axis=1)) + 1

print("Step-6")
print("Comparison table")
print(comparision(mat))
print("Step-7")
print("Object Scores")
print(score(mat))
print("Step-8")
print("Output")
print(Output(mat))

    
    


