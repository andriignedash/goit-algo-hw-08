import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Створюємо купу (мін-heap) з довжин кабелів
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    # Поки у купі більше одного елемента
    while len(cable_lengths) > 1:
        # Витягуємо два найменші елементи
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # Вартість з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost
        
        # Додаємо новий об'єднаний кабель назад до купи
        heapq.heappush(cable_lengths, cost)
    
    return total_cost

# Приклад використання
cable_lengths = [4, 3, 2, 6]
print(f"Мінімальні витрати на об'єднання кабелів: {min_cost_to_connect_cables(cable_lengths)}")
