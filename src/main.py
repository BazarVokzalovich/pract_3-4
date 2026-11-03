import os
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def run_block1_collisions():
    print("===== БЛОК 1 =====")
    N = 365
    k_values = [5, 10, 15, 20, 23, 30, 40, 50, 60, 70, 80]
    M = 10000
    
    stat_frequencies = []
    theoretical_probs = []
    
    for k in k_values:
        collision_count = 0
        for _ in range(M):
            sample = [random.randint(1, N) for _ in range(k)]
            if len(sample) != len(set(sample)):
                collision_count += 1
        
        w_collision = collision_count / M
        stat_frequencies.append(w_collision)
        
        p_no_collision = 1.0
        for i in range(k):
            p_no_collision *= (N - i) / N
        p_collision = 1.0 - p_no_collision
        theoretical_probs.append(p_collision)
        
        abs_error = abs(w_collision - p_collision)
        print(f"k = {k:2d} | Статистична: {w_collision:.4f} | Теоретична: {p_collision:.4f} | Похибка: {abs_error:.4f}")
    print()
    return k_values, stat_frequencies, theoretical_probs


def run_block3_monte_carlo():
    print("\n===== БЛОК 3 =====")
    N_values = [100, 1000, 10000, 100000, 1000000]
    exact_area = 0.181695
    
    mc_results = []
    
    for N in N_values:
        x_pts = np.random.rand(N)
        y_pts = np.random.rand(N)
        
        condition = (y_pts <= x_pts**2) & (y_pts >= 1.0 - x_pts)
        M = np.sum(condition)
        
        w_D = M / N
        mc_results.append(w_D)
        print(f"N = {N:7d} | Оцінка W(D) = {w_D:.6f} | Точна площа S(D) = {exact_area:.6f} | Похибка = {abs(w_D - exact_area):.6f}")
    print()
    return N_values, mc_results, exact_area


def plot_and_save_graphics(b1_data, b3_data):
    os.makedirs('graphics', exist_ok=True)
    k_vals, b1_stat, b1_th = b1_data
    N_vals, b3_stat, b3_exact = b3_data
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    print("===== БЛОК 1 - ГРАФІК =====")
    ax1.plot(k_vals, b1_th, 'r-', label='Теоретична ймовірність', linewidth=2)
    ax1.scatter(k_vals, b1_stat, color='blue', zorder=5, label='Статистична частота (M=10000)')
    ax1.set_title('Блок 1: Парадокс колізій (N=365)')
    ax1.set_xlabel('Кількість елементів (k)')
    ax1.set_ylabel('Ймовірність колізії')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend()
    
    print("\n===== БЛОК 3 - ГРАФІК =====")
    ax2.axhline(y=b3_exact, color='r', linestyle='-', label=f'Точне значення S(D) ({b3_exact})', linewidth=2)
    ax2.plot([str(n) for n in N_vals], b3_stat, 'b-o', label='Оцінка Монте-Карло')
    ax2.set_title('Блок 3: Збіжність методу Монте-Карло')
    ax2.set_xlabel('Кількість точок (N)')
    ax2.set_ylabel('Обчислена площа')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend()
    
    plt.tight_layout()
    graph_path = 'graphics/simulation_results.png'
    plt.savefig(graph_path)
    print(f"[УСПІХ] Графіки збережено у файл: {graph_path}")


if __name__ == '__main__':
    b1_outputs = run_block1_collisions()
    b3_outputs = run_block3_monte_carlo()
    plot_and_save_graphics(b1_outputs, b3_outputs)
