# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import random

class Visualization:
    
    def __init__(self):
        """
        数据可视化
        """
        ...
        
    def main(self):
        self.test()
        self.scatter_diagram()
        
    def scatter_diagram(self):
        """
        散点
        """
        
        plt.scatter(2, 10)
        plt.show()
        

    def test(self):
        """
        练习
        """
        squares = [1, 4, 9, 16, 25]
        # squares = [random.randint(10, 30) for item in range(10)]
        
        input_values = [1,2,3,4,5]
        
        print(input_values, squares)
        
        # linewidth 绘制线条粗细
        plt.plot(input_values, squares, linewidth=5)
        
        plt.title("Data View")
        plt.xlabel("Value", fontsize=19)
        plt.ylabel("Squares", fontsize=15)
        
        # 设置刻度标记大小
        plt.tick_params(axis='both', labelsize=14)
        
        # 查看图表
        plt.show()
        
if __name__ == "__main__":
    Visualization().main()