#include <assert.h>
#include <iostream>

using namespace std;

class Queue {
public:
	Queue(int lenght);
	~Queue();
	void	push_back(int data);
    int		pop_front();
    bool	is_empty();
private:
    int		size;
    int		head;
    int		tail;
    int		*que;
    int		get_size();
    void	init_que();
	void	increase_que();
	void	decrease_que();
};

Queue::Queue(int lenght) :
size(lenght),
head(0),
tail(0),
que(nullptr) {}

Queue::~Queue() {
    if (que != nullptr) {
        delete[] que;
	}
}

int		Queue::get_size() {
	if (tail < head) {
		return size - head + tail;
	} else {
		return tail - head;
	}
}

bool	Queue::is_empty() {
    return head == tail;
}

void	Queue::init_que() {
    que = new int[size];
}

void	Queue::increase_que() {
	int *buffer = new int[size * 2];
	for (int i = 0; i <= size - 2; i++) {
		buffer[i] = que[head];
		head = (head + 1) % size;
	}
	delete[] que;
	que = buffer;
	head = 0;
	tail = size - 1;
	size *= 2;
}

void	Queue::decrease_que() {
	int *buffer = new int[size / 2];
	int q_size = get_size();
	for (int i = 0; i <= q_size - 1; i++) {
		buffer[i] = que[head];
		head = (head + 1) % size;
	}
	delete[] que;
	que = buffer;
	head = 0;
	tail = q_size;
	size /= 2;
}

void	Queue::push_back(int data) {
    if (is_empty()) {
		init_que();
    }
    if (head == (tail + 1) % size) {
		increase_que();
    }
    que[tail] = data;
    tail = (tail + 1) % size;
}

int		Queue::pop_front() {
    assert(!is_empty());
    if (get_size() < size / 4 ) {
		decrease_que();
    }
    int answer = que[head];
    head = (head + 1) % size;
    return answer;
}

int main() {
    int n = 0;
	
    cin >> n;
    Queue myQueue(10);
    int count_true = 0;
    for (int i = 0; i < n; ++i) {
		int a, b;
        cin >> a >> b;
		switch (a) {
            case 2:
                if ((myQueue.is_empty() ? -1 : myQueue.pop_front()) == b) {
                    count_true += 1;
                }
                break;
            case 3:
                myQueue.push_back(b);
                count_true += 1;
                break;
		}
    }
    cout << (n == count_true ? "YES" : "NO");
    return 0;
}
