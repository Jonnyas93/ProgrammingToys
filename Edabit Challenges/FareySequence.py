def farey(n):
    result = {}
    denominator = n
    result[0/denominator] = "0/1"
    result[1] = "1/1"
    while denominator > 1:
        for i in range(1, denominator):
            
            if denominator%i == 0:
                #print("Simplify: "+str(i/i) + "/" + str(denominator/i))
                result[(i/denominator)]=(str(int(i/i)) + "/" + str(int(denominator/i)))
            else:
                #print("No simplify: "+str(i) + "/" + str(denominator))
                result[(i/denominator)]=(str(i) + "/" + str(denominator))
        denominator -= 1
    sortedResult = [value for key, value in sorted(result.items())]
    print(sortedResult)
    
if __name__ == "__main__":
    farey(1)
    farey(4)
    farey(5)