import numpy as np

def Colvolution(picture,filter_image):
    shape_big=picture.shape#picture need to filter
    shape_small=filter_image.shape#filter
    times_row=shape_big[0]-shape_small[0]+1#run times of row
    times_col=shape_big[1]-shape_small[1]+1##run times of column
    final=np.zeros((shape_big[0]-2,shape_big[1]-2))
    for row in range(0,times_row):
        for col in range(0,times_col):   
            tmp=filter_i*A[row:shape_small[0]+row,col:shape_small[1]+col,:]
            final[row,col]=tmp.sum()
    return final
if __name__=='__main__':
    A = np.array([
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,90,90,90,90,90,0,0],
        [0,0,0,90,90,90,90,90,0,0],
        [0,0,0,90,0,90,90,90,0,0],
        [0,0,0,90,90,90,90,90,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,90,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ])

    filter_i=np.array([
        [0,0,0],
        [0,2,0],
        [0,0,0]
    ])
    print(Colvolution(A,filter_i))
