import pygame

def bubble_sort(draw, _list: list[int]) -> None:
    n = len(_list)
    
    for i in range(n):
        swapped: bool = False
        
        for j in range(1, n):
            before: int = _list[j-1]
            current: int = _list[j]
            if before > current:
                _list[j-1], _list[j] = current, before # swap(_list, before, current)
                swapped = True
            
        if not swapped: break
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        draw()
                
def partition(_list, low, high):
    pivot = _list[high]
  
    i = low - 1

    for j in range(low, high):
        if _list[j] <= pivot:
            i = i + 1
            (_list[i], _list[j]) = (_list[j], _list[i])

    (_list[i + 1], _list[high]) = (_list[high], _list[i + 1])
    
    return i + 1

def quick_sort(draw, _list: list[int], low: int, high: int) -> None:
    draw()
    
    if low < high:
        p = partition(_list, low, high)
        quick_sort(draw, _list, low, p - 1)
        quick_sort(draw, _list, p + 1, high)