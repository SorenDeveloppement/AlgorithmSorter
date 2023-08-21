import pygame
import settings
import random
import threading

from swap import swap
from sorting_algo import bubble_sort, quick_sort
from algo_enum import AlgorithumEnum
from settings_window import SettingsWindow


pygame.display.init()
pygame.display.set_caption("Algorythm Sorter - SorenDev")
screen: pygame.Surface = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

def shake_list(_list: list) -> list:    
    for i in range(len(_list)):
        rdm_id2: int = random.randint(0, len(_list) - 1)
        swap(_list, _list[i], _list[rdm_id2])
        
    return _list
        

def draw(screen: pygame.Surface, values: list[int]) -> None:
    screen.fill(settings.BLACK)
    
    max_value: int = max(values)
    width: int = settings.WIDTH / len(values)
    
    for i, value in enumerate(values):
        height: int = (settings.HEIGHT * value) / max_value
        pygame.draw.rect(screen, settings.WHITE, (i * width, settings.HEIGHT - height, width, settings.HEIGHT))
    
    pygame.display.update()

def main() -> None:
    settings.LIST = shake_list([x for x in range(1, settings.LIST_LENGTH)])
    
    while True:
        draw(screen, settings.LIST)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    match settings.SELECTED_ALGO:
                        case AlgorithumEnum.BUBBLE:
                            bubble_sort(lambda: draw(screen, settings.LIST), settings.LIST)
                        case AlgorithumEnum.QUICK:
                            quick_sort(lambda: draw(screen, settings.LIST), settings.LIST, 0, len(settings.LIST) - 1)
                    draw(screen, settings.LIST)
                
                if event.key == pygame.K_r:
                    settings.LIST = shake_list([x for x in range(1, settings.LIST_LENGTH)])
                    draw(screen, settings.LIST)
                    
                if event.key == pygame.K_s:
                    # Aims to avoid an error message due to threading
                    def show_settings_win():
                        win = SettingsWindow(200, 200)
                        win.run()
                    # Aims to use the both windows at the same time
                    thread = threading.Thread(name= "Tkinter-AlgorithmSorterSettings", target=show_settings_win)
                    thread.start()
                

if __name__ == "__main__":
    main()