# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

from collections import deque

def deckRevealedIncreasing(deck):
    deck.sort()  
    queue = deque()

    for card in reversed(deck):  
        if queue:
            queue.appendleft(queue.pop())  
        queue.appendleft(card)  
    
    return list(queue)