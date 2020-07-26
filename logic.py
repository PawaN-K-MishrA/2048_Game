import random

#game starting function
def start_game():
    mat=[[0 for j in range(4)] for i in range(4)]
    return mat

#adding new 2 at random function
def add_new2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
    return mat
    
#getting the current state of function
def get_curr_state_of_game(mat):
    #if 2048 present you won
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
    #if 0 is presnet then game not over.
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'GAME NOT OVER.'
    #if same elemnts are present consceutively then also game not over.
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return 'GAME NOT OVER.'
    #checking consecutive for the last row.
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return 'GAME NOT OVER.'
    #checking consecutive for lastcolumn
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return 'GAME NOT OVER.'
    #if nither is true then game lost.
    return 'LOST'

#moving the non 0 elemnts left and 0 elements on right
def compress(mat):
    changed=False
    new_mat=[[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                #during the compress function the column index changes
                if j!=pos:
                    changed=True
                pos=pos+1
    return new_mat,changed

#merging the similar elements
def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            #if values are added then change is happening
            if mat[i][j] == mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
                changed=True
    return mat,changed
                
#reverse a matrix
def reverse(mat):
    rev_mat=[]
    for i in range(4):
        rev_mat.append(mat[i][::-1])
    return rev_mat

#transpose of mat
def transpose(mat):
    trans_mat=[[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            trans_mat[i][j]=mat[j][i]
    return trans_mat

def move_up(grid):
    transpose_grid=transpose(grid)
    new_grid,changed1=compress(transpose_grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    final_grid=transpose(new_grid)
    return final_grid,changed

def move_down(grid):
    transposed_grid=transpose(grid)
    reversed_grid=reverse(transposed_grid)
    new_grid,changed1=compress(reversed_grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    reversed_grid=reverse(new_grid)
    final_grid=transpose(reversed_grid)
    return final_grid,changed
    

def move_right(grid):
    reversed_grid=reverse(grid)
    new_grid,changed1=compress(reversed_grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    final_grid=reverse(new_grid)
    return final_grid,changed

def move_left(grid):
    new_grid,changed1=compress(grid)
    #print(new_grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    return new_grid,changed