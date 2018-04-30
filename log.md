# 100 Days Of Code - Log

### Day 0: April 26, 2018 (Example 1)


**Today's Progress**: Solved the first and second problems on projecteuler.net

**Thoughts:** Felt enjoyable to get code up and running so quickly.



### Day 1: April 27, 2018 


**Today's Progress**: Completed problems 3 through to 9 on projecteuler.net

**Thoughts**: Project 8 was quite satisfying as it was searching through a long list of digits that needed preparing.




### Day 2: April 28, 2018 - solved problems 10 and 11 on project euler.

**Today's Progress**: I've gone through many exercises on FreeCodeCamp.

**Thoughts** Another satisfying solution - a 400 list of numbers that needed multiplying horizontally, vertically and diagonally.

### Day 3: April 29, 2018 - Sunday - now I've met my match. Problem 12 is about finding a highly divisible triangle number. 

**Today's Progress**: This took a lot of effort - I need to look at the part that finds the divisible numbers.

**Thoughts** Another satisfying solution - a 400 list of numbers that needed multiplying horizontally, vertically and diagonally.


### Day 4: April 30, 2018 - Monday - Had trouble finding how to find all the divisors for a number, so had to steal a piece of code from Stackoverflow - I need to work out how it works. I created all the other code though 

```
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor```

**Today's Progress**:  Was quite pleased with the triangle number generator.

**Thoughts**
