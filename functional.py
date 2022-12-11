# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_and_sort('nameasdasd'))


# Make sure to answer the following questions about your coding process:
#Q-1 How does this solution ensure data immutability?
#A-1 I think so as it cant be altered in any way

#Q-2. Is this solution a pure function? Why or why not?
#A-2. This is not a pure function as the function relies on the side effects of being sorted and the output dose not depend purely on its input

#Q-3 Is this solution a higher order function? Why or why not?
#A-3 Yes it is a higher order function as it Accepts one or more functions as an argument

#Q-4 Would it have been easier to solve this problem using a different programming style?
#A-4 at this point im not sure I think it's probably around the same difficulty right now

#Q-5 Why in particular is functional programming a helpful paradigm when solving this problem?
#A-5 It helps us to solve problems effectively in a simpler way. 


