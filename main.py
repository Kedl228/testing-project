import requests
from pltdraw import PlotDrawer

url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"

def download_json(url, filename='deviation.json'):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Файл скачан и сохранен как {filename}")
    else:
        print(f"Не удалось скачать файл. Код ответа: {response.status_code}")

def main():
    download_json(url)

    plot_drawer = PlotDrawer('deviation.json')
    plot_drawer.draw_plots()

if __name__ == "__main__":
    main()
