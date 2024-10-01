import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class PlotDrawer:
    def __init__(self, json_file):
        # Загружаем данные из JSON файла
        self.data = pd.read_json(json_file)

    def draw_plots(self):
        # Создаём папку для графиков
        os.makedirs('plots', exist_ok=True)

        # График отклонений пола (floor) vs потолка (ceiling)
        self._draw_floor_vs_ceiling()

        # График для min vs max значений
        self._draw_min_vs_max()

    def _draw_floor_vs_ceiling(self):
        plt.figure(figsize=(18, 10))
        sns.lineplot(data=self.data, x='name', y='floor_mean', label='floor_mean', marker='o')
        sns.lineplot(data=self.data, x='name', y='ceiling_mean', label='ceiling_mean', marker='o')
        plt.title('Floor Mean vs Ceiling Mean')
        plt.xticks(rotation=45, ha='right', fontsize=4)
        plt.ylabel('Deviation (degrees)')
        plt.legend()
        plt.tight_layout()
        plot_path = os.path.join('plots', 'floor_vs_ceiling.png')
        plt.savefig(plot_path)
        #plt.show()
        plt.close()
        print(f"График сохранен: {plot_path}")

    def _draw_min_vs_max(self):
        plt.figure(figsize=(18, 10))
        sns.lineplot(data=self.data, x='name', y='min', label='min', marker='o')
        sns.lineplot(data=self.data, x='name', y='max', label='max', marker='o')
        plt.title('Min vs Max Deviation')
        plt.xticks(rotation=45, ha='right', fontsize=4)
        plt.ylabel('Deviation (degrees)')
        plt.legend()
        plt.tight_layout()
        plot_path = os.path.join('plots', 'min_vs_max.png')
        plt.savefig(plot_path)
        plt.close()
        print(f"График сохранен: {plot_path}")
