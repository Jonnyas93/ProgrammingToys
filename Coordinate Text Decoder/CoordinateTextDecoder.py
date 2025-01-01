import sys
import io
import pandas as pd
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def urlToCode(url):
    DF = []
    DF = pd.read_html(
        url, attrs={'class': 'c7'}, skiprows=1
    )
    xCoords = DF[0][0].copy().to_dict()
    yCoords = DF[0][2].copy().to_dict()
    chars = DF[0][1].copy().to_dict()
    y = sorted(yCoords.items(),key=lambda item: item[1],reverse=True)
    x = sorted(xCoords.items(),key=lambda item: item[1],reverse=True)
    height = int(y[0][1]) + 1
    length = int(x[0][1]) + 1
    output = [[" " for _ in range(length)] for _ in range(height)]
    for i in range(len(chars)):
        xt = int(xCoords.get(i))
        yt = int(yCoords.get(i))
        ct = chars.get(i)
        output[yt][xt] = ct
    outputString = ""
    for arr in output:
        outputString += "".join([s.replace('\n', '') for s in arr])
        outputString += "\n"
    print(outputString)

def main():
    urlToCode("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")

if __name__ == "__main__":
   main()