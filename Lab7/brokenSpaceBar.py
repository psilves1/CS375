def function(s, dictionary):
    result = []
    # gets max length of substr in dictionary
    max_l = len(max(dictionary, key=len))
    length = len(s)

    for back in range(1, length + 1):
        front = back - 1
        situation = 0
        goodStrs = []
        num = 0
        
        if back > max_l:
            num = back - max_l

        while(front >= num):
            if s[front:back] in dictionary:        
                #do we have a substring from front to back? 
                #if we do then lets continue on, otherwise this is a waste of time

                if (front > 0 and result[(front - 1)]): 
                    #for every valid substring [front:back], we're going to add our current 
                    for oldSubStr in result[front-1]:
                        goodStrs.append(oldSubStr + " " + s[front:back])

                    situation = 2
                else:
                    situation = 1
                    result.append([s[front:back]])

            front -= 1 #moves the front pointer one char to the left of the word
        
        if situation == 0:
            # no substrings found, appending empty list to symbolize that
            result.append([])
        if situation == 2:
            result.append(goodStrs)  # substring(s) found,
    if s in dictionary:
        result[len(s) - 1].append(s)

    return result[len(s) - 1]


# print(function("amango", {"a", "am", "an", "man", "go"}))
