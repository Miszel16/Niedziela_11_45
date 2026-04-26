# NIESTANDARDOWE STRUKTURY 

# 1. STOS
# - elementy w określonej kolejności
# - LIFO (Last In First Out)
# - np. historia przeglądania

# *(można zrobić za pomocą listy)

stack = []
stack.append('A')
stack.append('B')
stack.append('C')

print(f"Stos po dodaniu: {stack}\n") # A B C

element_top = stack.pop() # C

print(f"Top-element: {element_top}\nStos po zdjęciu elementu: {stack}\n") # A B


# 1.1. wizualizacja w paintcie

# 1.2. uwtorzenie własnej wersji struktury
# - dodawanie na stos [push] +
# - zdejmowanie ze stosu [pop] +
# - czy stos jest pusty? +
# - ile rzeczy na stosie? (rozmiar) +
# - co jest jako top? [peek] +

#  0  1  2  3
# -4 -3 -2 -1

class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop() # domyślnie usuwa ostatni element

    def is_empty(self):
        # if len(self.stack) == 0:
        #     return True
        # else:
        #     return False
        return len(self.stack) == 0 # True / False

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1] # ostatni element


print("\n\nStos:")
stos = Stack()
stos.push('D')
stos.push('K')
stos.push('O')
stos.push('T')

print(stos.pop()) # T
print(stos.peek()) # O
print(stos.size()) # 3
print(stos.is_empty()) # False




# ---------------------------------------------------------------------
# 2. KOLEJKA
# - elementy w koleności dodania
# - FIFO (First In First Out)
# - np. kolejka w sklepie

# 2.1. wizualizacja w paintcie

# 2.2. uwtorzenie własnej wersji struktury
# - dodawanie na koniec +
# - usuwanie z początku +
# - czy kolejka jest pusta? +
# - co jest na początku? +
# - ile rzeczy jest w kolejce? +


class Queue():
    def __init__(self):
        self.queue = []
    
    def add(self, item):
        self.queue.append(item)
    
    def is_empty(self):
        return len(self.queue) == 0 # True / False
    
    def delete(self):
        if not self.is_empty():
            return self.queue.pop(0)
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def size(self):
        return len(self.queue)
    

print("\n\nKolejka:")

kolejka = Queue()
kolejka.add("Kamil")
kolejka.add("Karol")
kolejka.add("Oskar")
kolejka.add("Paweł")
kolejka.add("Szymon")
kolejka.add("Tobiasz")


print(kolejka.delete()) # Kamil
print(kolejka.peek()) # Karol
print(kolejka.is_empty()) # False
print(kolejka.size()) # 5