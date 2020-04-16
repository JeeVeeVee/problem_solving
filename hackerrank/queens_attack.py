#n: an integer, the number of rows and columns in the board
#k: an integer, the number of obstacles on the board
#r_q: integer, the row number of the queen's position
#c_q: integer, the column number of the queen's position


def queensAttack(n, k, r_q, c_q, obstacles):
    r_q = r_q - 1
    c_q = c_q - 1
    veld = []
    for i in range(n):
        new_row = []
        for j in range(n):
            new_row.append(0)
        veld.append(new_row)

    veld[r_q][c_q] = "Q"

    diag_daal = r_q - c_q
    diag_stijg = c_q + r_q

    for obstacle in obstacles:
        if (obstacle[0] - obstacle[1] == diag_stijg):
            if obstacle[0] + obstacle[1] > r_q + c_q:
                for i in range(obstacle[0], n + 1):
                    veld[r_q + i][c_q + i] = -1
            else:
                #afbluvn
                for i in range(0, obstacle[0] + 1):
                    veld[i][obstacle[1] + i - 1] = -1
        elif (obstacle[1] + obstacle[0] == diag_daal):
            if (obstacle[0] - obstacle[1] < r_q - c_q):
                for i in range(0, n - max(obstacle[0], obstacle[1])):
                    veld[obstacle[0] - i][obstacle[1] +i] = -1
            else:
                for i in range(1, r_q):
                    veld[r_q + i][c_q + i] = -1

    for row in veld:
        print(row)

queensAttack(6, 4, 4, 3, [[1,4]])
