# Define a Function to compute Levenshtein Distance
def levdist(firstString, secondString):
    ''' Computes Levenshtein Distance between two Strings.
        input : two strings
        output : levenshtein distance
    '''
    # Write your code for the function here
    
    firstString = firstString.lower()
    secondString = secondString.lower()
    
    # Build a matrix of zeros for distance
    # Size 0f matrix = corresponding lengths of strings
    num_rows = len(firstString)
    num_cols = len(secondString)
    matrix = np.zeros([num_rows,num_cols])
    
    
     # Calculate distance based on the formula in wikipedia
    for row in range(num_rows):
        for col in range(num_cols):
            if firstString[row] == secondString[col]:
                not_equal = 0
            else:
                not_equal = 1
            
            if row == 0 and col == 0:
                del_dist = col+1 # length of second string till col index = col+1 as it starts from zero 
                ins_dist = row+1 # length of first string till row index = row+1 as it starts from zero
                sub_dist = 0 + not_equal
            
            elif row == 0:
                del_dist = (col+1) + 1
                ins_dist = matrix[row,col-1] + 1
                sub_dist = col + not_equal
                
            elif col== 0:
                del_dist = matrix[row-1,col] + 1
                ins_dist = (row+1) + 1
                sub_dist = row + not_equal
                
            else:
                
                del_dist = matrix[row-1,col] + 1
                ins_dist = matrix[row,col-1] + 1
                sub_dist = matrix[row-1,col-1] + not_equal
            
            
            
            matrix[row,col] = min(sub_dist,ins_dist,del_dist)


    print("Distance between {} and {} is {}".format(firstString,secondString,matrix[-1][-1]))
    return matrix[-1][-1]


# Call the Function
d=levdist("singapore", "indonesia")
d=levdist("kitten", "sitting")


