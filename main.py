# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2024/2/21
@Software: PyCharm
@disc:
======================================="""
import math
import time

import numpy as np
import pygame

# 定义网格大小
grid_size = (20, 20)

# 定义细胞状态
alive = 1
dead = 0
RECT_SIZE = 20

# 初始化网格
grid = np.random.randint(0, 2, size=grid_size)

# 定义邻居计数
neighbors = np.zeros(grid_size, dtype=np.int32)


def print_matrix(matrix, name: str = "矩阵打印"):
    n = math.ceil(matrix.shape[0] / 2)
    center = f" {name}{matrix.shape}={matrix.shape[0] * matrix.shape[1]} "
    print("-" * n + center + "-" * n)
    for row in matrix:
        print(row)
    print("-" * math.ceil(2 * n + len(center) * 1.25))


# 定义游戏规则
def game_of_life(grid, Evolution_times):
    """
    :param grid: 生命矩阵
    :param Evolution_times: 演化次数
    :return:
    """
    # 计算每个细胞的邻居数量
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            neighbors[i, j] = np.sum(grid[i - 1:i + 2, j - 1:j + 2])

    print_matrix(neighbors, "邻居数量矩阵")
    print("The %dth Evolution:" % evolution_times)
    # 更新每个细胞的状态
    # 审判死活
    last_alive_life_count = 0
    new_life_count = 0  # 复活数量
    mortality_count = 0  # 死亡数量
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if grid[i, j] == alive:
                last_alive_life_count += 1
                if neighbors[i, j] == 2 or neighbors[i, j] == 3:
                    # 如果一个活细胞周围有2或3个活细胞，则该细胞在下一代会继续存活。
                    grid[i, j] = alive
                else:
                    # 如果一个活细胞周围有0或1个活细胞，则该细胞在下一代会死亡。
                    grid[i, j] = dead
                    mortality_count += 1
            else:
                if neighbors[i, j] == 3:
                    # 如果一个死细胞周围有3个活细胞，则该细胞在下一代会复活。
                    grid[i, j] = alive
                    new_life_count += 1
    keep = last_alive_life_count - mortality_count
    left = new_life_count + keep
    print("死亡:", mortality_count, "存活:", keep, "诞生:", new_life_count,
          "最终生命单元:", left)
    print_matrix(grid, "新的生命矩阵")
    if mortality_count == 0 and new_life_count == 0:
        # 进入了稳态
        if left == 0:
            # 灭亡
            print("进过 {evolution_times} 次演化后, 该轮回遭到灭亡.")
        else:
            # 不再进化
            print(f"进过 {evolution_times} 次演化后, 该轮回不再进化(演化).")
        input("请键入任何案进行继续")


def render():
    # 渲染画面
    screen.fill((255, 255, 255))
    # 更新细胞
    for cell in cells:
        value = grid[cell.rect.x // RECT_SIZE, cell.rect.y // RECT_SIZE]
        # print(cell.rect, value)
        cell.color = (0, 0, 0) if value == dead else (0, 0, 255)
        pygame.draw.rect(screen, cell.color, cell.rect)
    pygame.display.flip()


if __name__ == '__main__':

    # 初始化 Pygame
    pygame.init()

    # 创建窗口
    screen = pygame.display.set_mode((grid_size[0] * RECT_SIZE, grid_size[1] * RECT_SIZE))
    # 设置窗口标题
    pygame.display.set_caption("Turing Utopia Experiment")

    # 设置背景颜色
    screen.fill((255, 255, 255))

    # 创建细胞
    cells = pygame.sprite.Group()

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            cell = pygame.sprite.Sprite()
            cell.rect = pygame.Rect(i * RECT_SIZE, j * RECT_SIZE, RECT_SIZE, RECT_SIZE)
            cell.color = (0, 0, 0) if grid[i, j] == dead else (0, 0, 255)
            cells.add(cell)
    render()
    print_matrix(grid, "种子生命矩阵 (初始种子)")
    input("Press any key to Start Evolution.")
    # 运行游戏
    running = True
    evolution_times = 0
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        evolution_times += 1
        # 更新游戏状态
        game_of_life(grid, evolution_times)
        # 把演化结果渲染到可视化界面中去
        render()
        time.sleep(1)

    # 退出 Pygame
    pygame.quit()
