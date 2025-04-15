# ANU CPB
Code developed for the CPB tutorial at ANU Cybernetics

# Deque: An Introduction to handling signals using Python

Imagine you have a line of people waiting for a service—like a queue at a movie theater—where people can enter or leave from both the front and the back. A **deque** (pronounced "D-q" or often "deck") in Python works like that line. It's a special list that lets you quickly add or remove items at either end:

- **Adding at the End:** Like a person joining at the back of the line.
- **Adding at the Front:** Like a person cutting in at the front.
- **Removing from the Front:** Like the person at the front leaving first (this is a queue).
- **Removing from the End:** Like the last person in the line being sent away (this is like a stack).

Because you can add or remove items quickly from both ends, a deque is perfect for situations where the order might change or you need to process things in both directions. It’s very efficient for these tasks, which means it gets the job done fast.

In everyday language, think of a deque as a super-flexible waiting line that doesn’t force you only to add or remove items at one end—it lets you do both almost instantly.

Below is a simple example of how you can use a deque in Python. This code demonstrates the basic operations, such as adding items to both ends and removing them, with comments that explain what each line does.

```python
# First, we import deque from the collections module.
from collections import deque

# Create an empty deque.
# Think of this as starting an empty line.
d = deque()

# Add items to the right end of the deque.
# This is like people joining the back of the line.
d.append('apple')
d.append('banana')

# Add an item to the left end of the deque.
# This is like someone cutting in at the front of the line.
d.appendleft('orange')

# At this point, the deque looks like: ['orange', 'apple', 'banana']
print("Deque after adding items:", list(d))

# Remove and return an item from the left end.
# This is like the first person in line leaving.
first_item = d.popleft()
print("Removed from the left:", first_item)

# Remove and return an item from the right end.
# This is like the last person in line leaving.
last_item = d.pop()
print("Removed from the right:", last_item)

# Display the remaining items in the deque.
print("Remaining items in deque:", list(d))
```

### Explanation in Simple Terms

1. **Importing Deque:**  
   We start by importing the special "deque" list from Python's collections library.

2. **Creating an Empty Deque:**  
   We create an empty deque called `d`, just like starting with an empty line.

3. **Adding Items:**  
   - We add "apple" and "banana" to the end (right side) of the deque.
   - We add "orange" to the start (left side).  
   The final order is `['orange', 'apple', 'banana']`.

4. **Removing Items:**  
   - We remove an item from the left side (the first item, "orange") and print it.
   - Then we remove an item from the right side (the last item, "banana") and print it.

5. **Showing What's Left:**  
   We print out what's left in the deque, which will be `['apple']`.
