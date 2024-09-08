import time
import multiprocessing


def read_info(name):
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            pass


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"{linear_duration:.6f} (линейный)")


    start_time = time.time()
    with multiprocessing.Pool(processes=6) as pool:
        pool.map(read_info, filenames)
    multi_process_duration = time.time() - start_time
    print(f"{multi_process_duration:.6f} (многопроцессный)")