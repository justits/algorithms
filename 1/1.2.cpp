#include <assert.h>
#include <iostream>

using namespace std;

class Deque {
public:
	Deque(int lenght);
	~Deque();
	void	push_front(int data);
	void	push_back(int data);
    int		pop_front();
	int		pop_back();
    bool	is_empty();
private:
    int		size;
    int		head;
    int		tail;
    int		*dec;
    int		get_size();
    void	init_dec();
	void	increase_dec();
	void	decrease_dec();
};

Deque::Deque(int lenght) :
size(lenght),
head(0),
tail(0),
dec(nullptr) {}

Deque::~Deque() {
    if (dec != nullptr) {
        delete[] dec;
	}
}

int		Deque::get_size() {
	if (tail < head) {
		return size - head + tail;
	} else {
		return tail - head;
	}
}

bool	Deque::is_empty() {
    return head == tail;
}

void	Deque::init_dec() {
    dec = new int[size];
}

void	Deque::increase_dec() {
	int *buffer = new int[size * 2];
	for (int i = 0; i <= size - 2; i++) {
		buffer[i] = dec[head];
		head = (head + 1) % size;
	}
	delete[] dec;
	dec = buffer;
	head = 0;
	tail = size - 1;
	size *= 2;
}

void	Deque::decrease_dec() {
	int *buffer = new int[size / 2];
	int d_size = get_size();
	for (int i = 0; i <= d_size - 1; i++) {
		buffer[i] = dec[head];
		head = (head + 1) % size;
	}
	delete[] dec;
	dec = buffer;
	head = 0;
	tail = d_size;
	size /= 2;
}

void	Deque::push_front(int data) {
    if (is_empty()) {
		init_dec();
    }
    if (head == (tail + 1) % size) {
		increase_dec();
    }
	head = (head == 0 ? size : head) - 1;
    dec[head] = data;
}

void	Deque::push_back(int data) {
    if (is_empty()) {
		init_dec();
    }
    if (head == (tail + 1) % size) {
		increase_dec();
    }
    dec[tail] = data;
    tail = (tail + 1) % size;
}

int		Deque::pop_front() {
    assert(!is_empty());
    if (get_size() < size / 4 ) {
		decrease_dec();
    }
    int answer = dec[head];
    head = (head + 1) % size;
    return answer;
}

int		Deque::pop_back() {
    assert(!is_empty());
    if (get_size() < size / 4 ) {
		decrease_dec();
    }
	tail = (tail == 0 ? size : tail) - 1;
    return dec[tail];
}

int main() {
    int n = 0;
	
    cin >> n;
    Deque myDeque(1);
    int count_true = 0;
    for (int i = 0; i < n; ++i) {
		int a, b;
        cin >> a >> b;
		switch (a) {
			case 1:
                myDeque.push_front(b);
                count_true += 1;
                break;
            case 2:
                if ((myDeque.is_empty() ? -1 : myDeque.pop_front()) == b) {
                    count_true += 1;
                }
                break;
            case 3:
                myDeque.push_back(b);
                count_true += 1;
                break;
			case 4:
				if ((myDeque.is_empty() ? -1 : myDeque.pop_back()) == b) {
					count_true += 1;
				}
				break;
		}
    }
    cout << (n == count_true ? "YES" : "NO");
    return 0;
}
