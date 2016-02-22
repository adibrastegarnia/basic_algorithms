def LCS(A,C):
    m = len(A)
    n = len(C)
    M = [[0 for col in range(n + 1)] for row in range(m + 1)]
    B = [[[0,0] for col in range(n + 1)] for row in range(m + 1)]
    
    for i in range(0, m):
        for j in range(0,n):
            if A[i] == C[j]:
                M[i][j] = M[i-1][j-1] + 1
                B[i][j] = [i,j]
            elif M[i-1][j] >= M[i][j-1]:
                M[i][j] = M[i-1][ j]
                B[i][j] = B[i-1][j]
            else:
                M[i][j] = M[i][j-1]
                B[i][j] = B[i][j-1]
                
    print_lcs(A,M,B, m - 1 , n- 1)


def LCS_three(X,Y,Z):
    n_x = len(X)
    n_y = len(Y)
    n_z = len(Z)
    
    M = [[[0 for k in xrange(n_z + 1)] for j in xrange(n_y + 1)] for i in xrange(n_x + 1)]
    B = [[[[0,0,0] for k in xrange(n_z + 1)] for j in xrange(n_y + 1)] for i in xrange(n_x + 1)]

    for i in range(0,n_x):
        for j in range(0, n_y):
            for k in range(0, n_z):
                if X[i] == Y[j] and X[i] == Z[k]:
                    M[i][j][k] = M[i-1][j-1][k-1] + 1
                    B[i][j][k]  = [i,j,k]
                else:
                    max_m = max(M[i-1][j][k], M[i][j-1][k], M[i][j][k-1])
                    if max_m == M[i-1][j][k]:
                        M[i][j][k] = M[i-1][j][k]
                        B[i][j][k] = B[i-1][j][k]
                    elif max_m == M[i][j-1][k]:
                        M[i][j][k] = M[i][j-1][k]
                        B[i][j][k] = B[i][j-1][k]
                    else:
                        M[i][j][k] = M[i][j][k-1]
                        B[i][j][k] = B[i][j][k-1]

    print_lcs_three(X, M,B, n_x - 1, n_y - 1, n_z - 1)


def print_lcs_three(A,M,B, i, j, k):
    if M[i][j][k] > 0:
        i_prime = B[i][j][k][0]
        j_prime = B[i][j][k][1]
        k_prime = B[i][j][k][2]
        print_lcs_three(A,M,B , i_prime-1, j_prime-1, k_prime-1)
        print(A[i_prime])


    
def print_lcs(A,M,B, i,j):
    if M[i][j] > 0:
        i_prime = B[i][j][0]
        j_prime = B[i][j][1]
        print_lcs(A,M,B, i_prime - 1,j_prime-1)
        print(A[i_prime])


def main():
   A = "abbcd"
   B = "bbddc"
   C = "bdghi"
   X = "ENTROPY"
   Y = "THORNY"
   Z = "TROP"
   LCS(X,Y)
   #LCS_three(A,B,C)
   #LCS_three(X,Y,Z)


   


main()
