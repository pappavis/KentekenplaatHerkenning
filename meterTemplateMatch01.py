import imghdr
from re import template
from tempfile import tempdir
from traceback import print_tb
import traceback
from unittest import result
import cv2
import os
from pathlib import PurePath
import random
import numpy as np
import time
import pytesseract
#OpenCV Python zoek overeenstemmend in een opgegevn plaatje.
#ref --> https://youtu.be/T-0lZWYWE9Y?list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn
#20220630

class clsMain:
    def __init__(self) -> None:
        self.img = None
        self.cap = None
        self.scriptFull = PurePath(__file__)
        self.scriptPath = str(PurePath(self.scriptFull.parent))

    def main(self):
        '''Main routine'''

        templateToUse = f'''{self.scriptPath}/assets/meterstand_template_leeg.jpg'''
        plaatjesDict = [{"imgSrc1" : f'''{self.scriptPath}/assets/meterstand_elektra20220630_test1.jpg''',
                         "imgTemplateSr1" : templateToUse},
                         {"imgSrc1" : f'''{self.scriptPath}/assets/meterstand_elektra20220630_test2.jpg''',
                         "imgTemplateSr1" : templateToUse}
                         ]

        try:
            for item1 in plaatjesDict:
                imgSrc1 = item1["imgSrc1"]
                imgTemplateSr1 = item1["imgTemplateSr1"]

                npUitgeknipt, rect1 = self.getCroppedImageFromTemplate(imgSrc=imgSrc1, imgTemplate=imgTemplateSr1)

                cv2.imwrite(f'''{self.scriptPath}/assets/resultaat_meterTemplateMatch01_rect1.jpg''', rect1)
                cv2.imshow(f'rect1=versie', rect1)
                cv2.waitKey(2000)

                resultImg = f'''{self.scriptPath}/assets/resultaat_meterTemplateMatch01_npUitgeknipt.jpg'''
                cv2.imwrite(f'''{resultImg}''', npUitgeknipt)
                cv2.imshow(f'npUitgeknipt=versie', npUitgeknipt)
                cv2.waitKey(2000)

                cv2.destroyAllWindows()

                ocrStr = pytesseract.image_to_string(resultImg)
                print(f'''OCRed={ocrStr}''')


        except Exception as ex1:
            print(traceback.print_exc())
        finally:
            cv2.destroyAllWindows()


    def getCroppedImageFromTemplate(self, imgSrc, imgTemplate):
        '''getCroppedImageFromTemplate(imgSrc, imgTemplate) -> retval\n.   @brief zoek de desbetreffend beeld in de opgegeven plaatje.  ideaal voor meterstanden uitlezen. @param imgSrc BronplaatjeJPG   @param imgTemplate hetgeen je zoekt in de plaaatje RETURNS: npArray'''
        npImgSrc1 = cv2.imread(f'''{imgSrc}''', cv2.IMREAD_GRAYSCALE)
        npTemplate1 = cv2.imread(f'''{imgTemplate}''', cv2.IMREAD_GRAYSCALE)

        h, w = npTemplate1.shape   #hoogte is array van element startpunt boven en eindpunt onder, w=start element links, naar rechts.
        #voor shapes, zie turital https://www.tutorialspoint.com/numpy/numpy_indexing_and_slicing.htm


        methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
                    cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

        teller0 = 1
        npUitgeknipt = None
        rect1 = None

        try:
            print(f'''Maak een copy van {npImgSrc1}''')
            npImgSrc1copy = npImgSrc1.copy()
            method = cv2.TM_CCOEFF_NORMED

            print(f'''Zoek de overeenkomst {imgTemplate} in bron={imgSrc}''')

            matchResult = cv2.matchTemplate(image=npImgSrc1, templ=npTemplate1, method=method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchResult)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                location = min_loc
            else:
                location = max_loc

            print(f'''Overeenstemmend beeld wordt getoond: {matchResult}''')
            cv2.imshow(f'matchResult getoond', matchResult)
            cv2.waitKey(2000)

            bottom_right = (location[0] + w, location[1] + h)    
            npUitgeknipt = npImgSrc1copy[location[1]:bottom_right[1], location[0]:bottom_right[0]]        
            rect1 = cv2.rectangle(npImgSrc1copy, location, bottom_right, 255, thickness=5)
            
        except Exception as ex1:
            print(traceback.print_exc())
        finally:
            cv2.destroyAllWindows()

        return npUitgeknipt, rect1


if __name__ == "__main__":
    print("App start")
    main1 = clsMain()
    main1.main()
    print("App eind")