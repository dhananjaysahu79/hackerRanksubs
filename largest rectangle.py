def largestRectangle(arr):
    maxi = 0
    stack = []
    # add 0 at last as in case when height is strictly increasing we need to stop at end to evalute.
    arr.append(0)
    for i in range(len(arr)):
        left = i
        while len(stack) and arr[i] < stack[-1][0]:
            left = stack[-1][1]
            # calclating area from the index where we stopped taking constant height as the height is lower till this while loop executes
            # why taking +1??
            # as we included the current index height too
            maxi = max(maxi, (i - stack[-1][1] + 1) * arr[i])
            # so i is the end point for all the heights till the while loop executes.
            # so we will calculate the areas for all the stack elements one by one and pop them out.
            maxi = max(maxi, (i - stack[-1][1]) * stack[-1][0])
            # poping out to reduce the complexity.
            stack.pop()
        # now why adding left instead of height's original index?
        # as we have reduced our stack by eleminating all the elements greater than the current height, it is obvious that our current height would cross those bigger elements in the left that we have removed to make its area. so have to update the counts of the elements that we poped.
        stack.append([arr[i],left])
    return maxi