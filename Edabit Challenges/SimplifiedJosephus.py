#Solving a simplified version of the Josephus problem, where n is num and k is always 2
def simplified_josephus(num):
    # Initialize the circle with people numbered from 1 to num
    circle = []
    for i in range(1, num + 1):
        circle.append(i)

    # Start at the first person
    index = 0

    # Continue until only one person is left
    while len(circle) > 1:
        #print ("Circle Size:" + str(len(circle)) + " | Circle: " + str(circle))
        if index < len(circle) - 1:
            #print("Number "+ str(circle[index]) + " shot: " + str(circle[index+1]))
            # Remove the next person in the circle
            circle.pop(index + 1)
            # Update the index to the next person
            if (index + 1) >= len(circle):
                index = 0
            else:
                index += 1
        else:
            #print("Number "+ str(circle[index]) + " shot: " + str(circle[0]))
            # If the current index is the last person, remove the first person
            circle.pop(0)
            # Reset the index to the start of the circle
            index = 0

    # Return the last remaining person
    return circle[0]

if __name__ == "__main__":
    print(simplified_josephus(1))
    print(simplified_josephus(8))
    print(simplified_josephus(41))
