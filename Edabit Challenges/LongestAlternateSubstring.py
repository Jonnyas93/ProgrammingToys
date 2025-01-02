import sys
import io
from collections import deque

def longest_substring(string):
    longestQueue = deque()
    currentQueue = deque()
    for i in range(len(string) - 1):
        if len(currentQueue) == 0:
            currentQueue.append(string[i])
        else:
            if (int(string[i])%2 == 0 and int(currentQueue[-1])%2 != 0):
                currentQueue.append(string[i])
            elif(int(string[i])%2 != 0 and int(currentQueue[-1])%2 == 0):
                currentQueue.append(string[i])
            else:
                if len(currentQueue) > len(longestQueue):
                    longestQueue.clear()
                    longestQueue.extend(currentQueue)
                currentQueue.clear()
                currentQueue.append(string[i])
    print("".join(longestQueue))
    
if __name__ == "__main__":
    longest_substring("225424272163254474441338664823")
    longest_substring("594127169973391692147228678476")
    longest_substring("721449827599186159274227324466")