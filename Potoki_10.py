from threading import Thread
import time

start_time = time.time()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f'Какое-то слово № {i}'
            file.write(word + '\n')
            time.sleep(0.1)
            print(f' Завершилась запись в файл {file_name}')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Работа потоков {elapsed_time:.2f} секунд')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

threads = []
thread_args = [(10, "example5.txt"), (30, "example6.txt"), (200, "example7.txt"), (100, "example8.txt")]

for args in thread_args:
    thread = Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
