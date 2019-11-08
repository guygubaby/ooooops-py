import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


lock = Lock()

def run(word):
  with lock:
    with open('test.txt','a+') as f:
      f.write(str(word)+ ' ')


if __name__ == "__main__":
    start = time.time()
    lst = [2,4,23,4,23,4,234,3,234,3]
    with ThreadPoolExecutor(len(lst)) as executor:
      executor.map(run,lst)
    print('time used : {}'.format(time.time()-start))

    # 0.5055649280548096