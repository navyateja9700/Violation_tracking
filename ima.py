# in this code we have opened an image then drawed a box around the bike and found the exact widtgh and height of box
import cv2

img=cv2.imread(r'C:\Users\user\OneDrive\Desktop\Violation_tracking\a.jpg')
if img is None:
    print("this is worst")
else:
    # cv2.rectangle(img, (550, 800), (800, 300), (0, 255, 0), 3)
    cv2.rectangle(img, (450, 800), (700, 70), (0, 255, 0), 3)
    cv2.putText(img, 'No Helmet!', (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 
            1, (0, 0, 255), 2)

    # Show the image
    cv2.imshow('Image with Rectangle and Text', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# Show the image
    # cv2.imshow('Image with Rectangle', img)
    # cv2.waitKey(0)
