def farey(n):
    result = {}
    denominator = n
    result[0/denominator] = "0/" + str(denominator)
    while denominator >= 1:
        for i in range(1, n):
            if denominator%i == 0:
                result[(i/denominator)]=(str(i/i) + "/" + str(denominator/i))
            else:
                result[(i/denominator)]=(str(i) + "/" + str(denominator))
        denominator -= 1
    sortedResult = [value for key, value in sorted(result.items())]
    print(sortedResult)
    
if __name__ == "__main__":
    farey(1)
    farey(4)
    farey(5)