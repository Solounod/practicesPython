
matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

new_matriz = [[row[i] for row in matriz] for i in range(4)]
print(new_matriz)


transpuesta = []

#for i in range(4):
#    print(i)
#    transpuesta.append([row[i] for row in matriz])

#print(transpuesta)


for i in range(4):
    transpuesta_row = []
    for row in matriz:
        
        transpuesta_row.append(row[i])
        print(transpuesta_row)
    transpuesta.append(transpuesta_row)

#[1]
#[1, 5]
#[1, 5, 9]
#[2]
#[2, 6]
#[2, 6, 10]
#[3]
#[3, 7]
#[3, 7, 11]
#[4]
#[4, 8]
#[4, 8, 12]

