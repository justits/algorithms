#include <assert.h>
#include <iostream>

using namespace std;

template <typename T>
class Deque {
public:
	Deque(size_t lenght);
	~Deque();
	bool	is_empty();
	void	push_front(T data);
	void	push_back(T data);
	T		pop_front();
	T		pop_back();
private:
	size_t	size;
	size_t	head;
	size_t	tail;
	T		*dec;
	size_t	get_size();
	void	init_dec();
	void	increase_dec();
	void	decrease_dec();
};

template <typename T>
Deque<T>::Deque(size_t lenght) :
size(lenght),
head(0),
tail(0),
dec(nullptr) {}

template <typename T>
Deque<T>::~Deque() {
	if (dec != nullptr) {
		delete[] dec;
	}
}

template <typename T>
size_t	Deque<T>::get_size() {
	if (tail < head) {
		return size - head + tail;
	} else {
		return tail - head;
	}
}

template <typename T>
bool	Deque<T>::is_empty() {
	return head == tail;
}

template <typename T>
void	Deque<T>::init_dec() {
	dec = new T[size];
}

template <typename T>
void	Deque<T>::increase_dec() {
	T	*buffer = new T[size * 2];
	for (size_t i = 0; i <= size - 2; i++) {
		buffer[i] = dec[head];
		head = (head + 1) % size;
	}
	delete[] dec;
	dec = buffer;
	head = 0;
	tail = size - 1;
	size *= 2;
}

template <typename T>
void	Deque<T>::decrease_dec() {
	T	*buffer = new T[size / 2];
	size_t d_size = get_size();
	for (size_t i = 0; i <= d_size - 1; i++) {
		buffer[i] = dec[head];
		head = (head + 1) % size;
	}
	delete[] dec;
	dec = buffer;
	head = 0;
	tail = d_size;
	size /= 2;
}

template <typename T>
void	Deque<T>::push_front(T data) {
	if (is_empty()) {
		init_dec();
	}
	if (head == (tail + 1) % size) {
		increase_dec();
	}
	head = (head == 0 ? size : head) - 1;
	dec[head] = data;
}

template <typename T>
void	Deque<T>::push_back(T data) {
	if (is_empty()) {
		init_dec();
	}
	if (head == (tail + 1) % size) {
		increase_dec();
	}
	dec[tail] = data;
	tail = (tail + 1) % size;
}

template <typename T>
T		Deque<T>::pop_front() {
	assert(!is_empty());
	if (get_size() < size / 4 ) {
		decrease_dec();
	}
	T	answer = dec[head];
	head = (head + 1) % size;
	return answer;
}

template <typename T>
T		Deque<T>::pop_back() {
	assert(!is_empty());
	if (get_size() < size / 4 ) {
		decrease_dec();
	}
	tail = (tail == 0 ? size : tail) - 1;
	return dec[tail];
}

int		main() {
	size_t	n;
	cin >> n;
	Deque<int> myDeque(2);
	size_t	count_true = 0;
	for (size_t i = 0; i < n; ++i) {
		int a, b;
		cin >> a >> b;
		switch (a) {
			case 1:
				myDeque.push_front(b);
				count_true++;
				break;
			case 2:
				if ((myDeque.is_empty() ? -1 : myDeque.pop_front()) == b) {
					count_true++;
				}
				break;
			case 3:
				myDeque.push_back(b);
				count_true++;
				break;
			case 4:
				if ((myDeque.is_empty() ? -1 : myDeque.pop_back()) == b) {
					count_true++;
				}
				break;
		}
	}
	cout << (n == count_true ? "YES" : "NO");
	return 0;
}
