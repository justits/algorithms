#include <assert.h>
#include <iostream>

using namespace std;

template <typename T>
class Stack {
public:
	Stack(size_t lenght);
	~Stack();
	bool	is_empty();
	void	push(T data);
    T		pop();
private:
    size_t	size;
	size_t	head;
    T		*stack;
	void	init_stack();
	void	increase_stack();
	void	decrease_stack();
};

template <typename T>
Stack<T>::Stack(size_t lenght) :
size(lenght),
head(0),
stack(nullptr) {
	init_stack();
}

template <typename T>
Stack<T>::~Stack() {
	if (stack != nullptr) {
        delete[] stack;
	}
}

template <typename T>
void	Stack<T>::init_stack() {
	stack = new T[size];
}

template <typename T>
void	Stack<T>::increase_stack() {
	T *buffer = new T[size * 2];
	for (size_t i = 0; i < size; i++) {
		buffer[i] = stack[i];
	}
	delete[] stack;
	stack = buffer;
	size *= 2;
}

template <typename T>
void	Stack<T>::decrease_stack() {
	T *buffer = new T[size / 2];
	for (size_t i = 0; i < size / 4; i++) {
		buffer[i] = stack[i];
	}
	delete[] stack;
	stack = buffer;
	size /= 2;
}

template <typename T>
bool	Stack<T>::is_empty() {
	return head == 0;
}

template <typename T>
void	Stack<T>::push(T data) {
	if (head == size - 1) {
		increase_stack();
	}
	head++;
	stack[head] = data;
}

template <typename T>
T		Stack<T>::pop() {
	assert(!is_empty());
	T	answer = stack[head];
	head--;
	if (head < size / 4) {
		decrease_stack();
	}
	return answer;
}

template <typename T>
class Queue {
public:
	Queue(size_t lenght);
	bool		is_empty();
	void		push_back(T data);
    T			pop_front();
private:
	Stack<T>	left;
	Stack<T>	right;
};

template <typename T>
Queue<T>::Queue(size_t lenght) :
left(lenght),
right(lenght) {}

template <typename T>
bool	Queue<T>::is_empty() {
    return left.is_empty() && right.is_empty();
}

template <typename T>
void	Queue<T>::push_back(T data) {
	left.push(data);
}

template <typename T>
T		Queue<T>::pop_front() {
	assert(!is_empty());
	if (right.is_empty()) {
		while (!left.is_empty()) {
			right.push(left.pop());
		}
	}
	return right.pop();
}

int		main() {
    size_t n;
    cin >> n;
    Queue<int> myQueue(2);
    size_t count_true = 0;
    for (size_t i = 0; i < n; ++i) {
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
