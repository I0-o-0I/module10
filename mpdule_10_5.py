from multiprocessing import Pool
import datetime
def read_info(name):
    all_data = []
    with open(name, "r", encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]
times1 = datetime.datetime.now()
for name in filenames:
    read_info(name)
timee1 = datetime.datetime.now()
print('линейный', timee1-times1)
#if __name__ == '__main__':
#    times2 = datetime.datetime.now()
#    with Pool(4) as p:
#       p.map(read_info, filenames)
#    timee2 = datetime.datetime.now()
#    print('многопроц', timee2-times2)