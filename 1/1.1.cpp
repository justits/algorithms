#include <assert.h>
#include <iostream>

using namespace std;

template <typename T>
class Queue {
public:
	Queue(size_t lenght);
	~Queue();
	bool	is_empty();
	void	push_back(T data);
	T		pop_front();
private:
	size_t	size;
	size_t	head;
	size_t	tail;
	T		*que;
	size_t	get_size();
	void	init_que();
	void	increase_que();
	void	decrease_que();
};

template <typename T>
Queue<T>::Queue(size_t lenght) :
size(lenght),
head(0),
tail(0),
que(nullptr) {}

template <typename T>
Queue<T>::~Queue() {
	if (que != nullptr) {
		delete[] que;
	}
}

template <typename T>
size_t		Queue<T>::get_size() {
	if (tail < head) {
		return size - head + tail;
	} else {
		return tail - head;
	}
}

template <typename T>
bool	Queue<T>::is_empty() {
	return head == tail;
}

template <typename T>
void	Queue<T>::init_que() {
	que = new T[size];
}

template <typename T>
void	Queue<T>::increase_que() {
	T *buffer = new T[size * 2];
	for (size_t i = 0; i <= size - 2; i++) {
		buffer[i] = que[head];
		head = (head + 1) % size;
	}
	delete[] que;
	que = buffer;
	head = 0;
	tail = size - 1;
	size *= 2;
}

template <typename T>
void	Queue<T>::decrease_que() {
	T *buffer = new T[size / 2];
	size_t q_size = get_size();
	for (size_t i = 0; i <= q_size - 1; i++) {
		buffer[i] = que[head];
		head = (head + 1) % size;
	}
	delete[] que;
	que = buffer;
	head = 0;
	tail = q_size;
	size /= 2;
}

template <typename T>
void	Queue<T>::push_back(T data) {
	if (is_empty()) {
		init_que();
	}
	if (head == (tail + 1) % size) {
		increase_que();
	}
	que[tail] = data;
	tail = (tail + 1) % size;
}

template <typename T>
T		Queue<T>::pop_front() {
	assert(!is_empty());
	if (get_size() < size / 4 ) {
		decrease_que();
	}
	T	answer = que[head];
	head = (head + 1) % size;
	return answer;
}

int		main() {
	size_t	n;
	cin >> n;
	Queue<int> myQueue(2);
	size_t	count_true = 0;
	for (size_t i = 0; i < n; ++i) {
		int a, b;
		cin >> a >> b;
		switch (a) {
			case 2:
				if ((myQueue.is_empty() ? -1 : myQueue.pop_front()) == b) {
					count_true++;
				}
				break;
			case 3:
				myQueue.push_back(b);
				count_true++;
				break;
		}
	}
	cout << (n == count_true ? "YES" : "NO");
	return 0;
}
