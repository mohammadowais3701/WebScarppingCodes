from PIL import Image
import subprocess

def cleanFile(filePath,outputFile):
    image=Image.open(filePath)
    image=image.point(lambda x:0 if x<143 else  255)
    image.save(outputFile)
    subprocess.call(["C:\\Program Files\\Tesseract-OCR\\tesseract",outputFile,"output"])
    output=open("output.txt","r")
    print(output.read())
    output.close()
cleanFile("text2.png",'text2_clean.png')