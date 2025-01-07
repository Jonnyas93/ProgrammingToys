import sys
import io
import pandas as pd
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#this was a coding challenge where a secret message was spelled out with different shaded boxes, that had to be arranged according to coordinates. 

def urlToCode(url):
    DF = []
    DF = pd.read_html(
        url, attrs={'class': 'c7'}, skiprows=1
    )#scrape the data from the url and put it into a panda DataFrame
    xCoords = DF[0][0].copy().to_dict()#separate out the different coordinates and characters into 3 dictionaries with the same indexing
    yCoords = DF[0][2].copy().to_dict()
    chars = DF[0][1].copy().to_dict()
    y = sorted(yCoords.items(),key=lambda item: item[1],reverse=True)#sort the x and y coordinates so we can calculate the size of the image
    x = sorted(xCoords.items(),key=lambda item: item[1],reverse=True)
    height = int(y[0][1]) + 1 #calculate the height of the output string
    length = int(x[0][1]) + 1 #calculate the length of the output string
    output = [[" " for _ in range(length)] for _ in range(height)]#Create a 2D array that is the length and height we just calculated
    for i in range(len(chars)):#going through each character, get the corresponding coordinates for that character, and then put that character in the 2D array at the corresponding coordinates
        xt = int(xCoords.get(i))
        yt = int(yCoords.get(i))
        ct = chars.get(i)
        output[yt][xt] = ct
    outputString = ""#Create a string to be filled with the values from the 2D array
    for arr in output:#go through each row in the 2D array and combine them together, adding a newline at the end of each row
        outputString += "".join([s.replace('\n', '') for s in arr])
        outputString += "\n"
    print(outputString)

def main():
    urlToCode("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")

if __name__ == "__main__":
   main()