from collections import deque


if __name__ == "__main__":
    q = deque(maxlen=2)
    q.append(1)
    q.appendleft(2)
    q.append('234')
    print(q)