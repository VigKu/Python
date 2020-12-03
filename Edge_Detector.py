# Import the image in NumPy and convert to Grayscale
# Choose target image processing task and the kernel
# Perform convolution with the image and your kernel
# Display the original and the final grayscale image

def imgRead():
    '''
        Read image from path
    '''
    while 1:
        try:
            path = input("Please enter image path: ")
            po = plt.imread(path)
            return po
        except:
            print("Please check if path is valid!")
            continue


def rgb2gray(po):
    '''
        Converts to gray image
    '''
    po_gray = np.dot(po[:,:,0:3], [0.299, 0.587, 0.114])
    return po_gray

def plotGrayPo(po,po_gray,po_edgedetect):
    '''
        Plots 2 images side by side
    '''
    #plt.imshow(po_gray, cmap=plt.get_cmap('gray'))
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(16,8))
    axs[0].imshow(po)
    axs[1].imshow(po_gray, cmap=plt.get_cmap('gray'))
    axs[2].imshow(po_edgedetect, cmap=plt.get_cmap('gray'))
    
def applyEdgeDetection(img):
    '''
        Performs edge detection on the image with 3x3 kernel of following weight:
        # -1 -1 -1
        # -1  8 -1
        # -1 -1 -1
    '''
    
    print("-------------\n")
    print("Kernel used to detect edge:")
    print("-1 -1 -1\n")
    print("-1  8 -1\n")
    print("-1 -1 -1\n")
    print("-------------\n")

    # Build weights (kernel)
    filter_size = 3
    weights = np.ones([filter_size,filter_size])
    weights = weights*-1
    mid = (filter_size-1)//2
    weights[mid,mid] = 8
    
    # Get new image shape
    new_row = img.shape[0]-filter_size+1
    new_col = img.shape[1]-filter_size+1
        
    # Create new image with zeros
    res_img = np.zeros([new_row,new_col])
        
    # Perform masking
    for i in range(new_row):
        for j in range(new_col):
            patch = img[i:i+filter_size, j:j+filter_size]
            res_patch = patch*weights
            res_img[i,j] = np.sum(res_patch)/9 # naromalize with 9
            
    return res_img

def detectEdge():
    '''
        All in 1 function
    '''
    #path = "files/poDumpling.jpg"
    po = imgRead()
    po_gray = rgb2gray(po)
    po_edgedetect = applyEdgeDetection(po_gray)
    plotGrayPo(po,po_gray,po_edgedetect)


# Call for function
detectEdge()