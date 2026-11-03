import random
import math

def run_block2_variant3(num_simulations=100000):
    print("===== БЛОК 2 - Варіант 3 =====")
    p_A_th = 0.2778
    p_B_th = 0.1667
    p_AnB_th = 0.0463
    p_AuB_th = 0.3981
    p_notA_th = 0.7222

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
    
    count_A = 0
    count_B = 0
    count_AnB = 0
    count_AuB = 0
    count_notA = 0

    for _ in range(num_simulations):
        token = random.choices(alphabet, k=4)
        
        is_A = len(set(token)) == 4
        is_B = token[0] == 'A'

        if is_A: count_A += 1
        if is_B: count_B += 1
        if is_A and is_B: count_AnB += 1
        if is_A or is_B: count_AuB += 1
        if not is_A: count_notA += 1

    w_A = count_A / num_simulations
    w_B = count_B / num_simulations
    w_AnB = count_AnB / num_simulations
    w_AuB = count_AuB / num_simulations
    w_notA = count_notA / num_simulations

    print(f"Кількість симуляцій: {num_simulations}")
    print(f"Подія A (всі різні) | Статистична: {w_A:.4f} | Теоретична: {p_A_th:.4f} | Похибка: {abs(w_A - p_A_th):.4f}")
    print(f"Подія B (старт з A  | Статистична: {w_B:.4f} | Теоретична: {p_B_th:.4f} | Похибка: {abs(w_B - p_B_th):.4f}")
    print(f"Перетин A ∩ B       | Статистична: {w_AnB:.4f} | Теоретична: {p_AnB_th:.4f} | Похибка: {abs(w_AnB - p_AnB_th):.4f}")
    print(f"Об'єднання A U B    | Статистична: {w_AuB:.4f} | Теоретична: {p_AuB_th:.4f} | Похибка: {abs(w_AuB - p_AuB_th):.4f}")
    print(f"Доповнення ~A       | Статистична: {w_notA:.4f} | Теоретична: {p_notA_th:.4f} | Похибка: {abs(w_notA - p_notA_th):.4f}")
    print(f"Перевірка ПР ТЙ P(~A) = 1 - P(A): {w_notA:.4f} ≈ 1 - {w_A:.4f} = {1 - w_A:.4f}\n")

def run_block4_variant3():
    print("===== БЛОК 4 - Варіант 3 =====")
    N = 65536
    k = 200
    M = 10000
    
    p_theoretical = 0.2630
    
    collision_sessions_count = 0
    
    for _ in range(M):
        sessions = [random.randint(0, N - 1) for _ in range(k)]
        if len(sessions) != len(set(sessions)):
            collision_sessions_count += 1
            
    w_collision = collision_sessions_count / M
    abs_error = abs(w_collision - p_theoretical)
    
    print(f"Змодельовано сесій: {M}")
    print(f"Знайдена статистична частота колізій: {w_collision:.4f}")
    print(f"Теоретична ймовірність за лекцією:    {p_theoretical:.4f}")
    print(f"Абсолютна похибка результату:         {abs_error:.4f}\n")

if __name__ == '__main__':
    run_block2_variant3(num_simulations=100000)
    run_block4_variant3()
