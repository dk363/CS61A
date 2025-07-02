打包传递参数
```
def make_averaged(original_function, times_called=1000):

    """Return a function that returns the average value of ORIGINAL_FUNCTION

    called TIMES_CALLED times.

  

    To implement this function, you will have to use *args syntax.

  

    >>> dice = make_test_dice(4, 2, 5, 1)

    >>> averaged_dice = make_averaged(roll_dice, 40)

    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's

    3.0

    """

    # BEGIN PROBLEM 8

    "*** YOUR CODE HERE ***"

    def averaged_roll_dice(*args):

        total = 0

        for i in range(times_called):

            total += original_function(*args)

        return total / times_called

    return averaged_roll_dice

    # END PROBLEM 8
```

