#include <assert.h>
#include <iostream>

using namespace std;

template <typename T>
class Heap {
public:
	Heap(int size, T* elements);
	int	size;
	T		get(int index);
	T		pop(int index);
	void	push(T data);
private:
	int	buf_size;
	T*		heap;
	bool	empty();
	void	build_heap();
	void	sift_down(int index);
	void	sift_up(int index);
	void	increase_dec();
	void	decrease_dec();
};

template <typename T>
Heap<T>::Heap(int size, T* elements) :
size(size),
buf_size(size),
heap(elements) {
	build_heap();
}

template <typename T>
bool	Heap<T>::empty() {
	return size == 0;
}

template <typename T>
void	Heap<T>::build_heap() {
	for (int i = size / 2 + 1 ; i > 0 ; i--) {
		sift_down(i - 1);
	}
}

template <typename T>
void	Heap<T>::sift_down(int index) {
	int left = 2 * index + 1;
	int right = 2 * index + 2;
	int largest = index;
	if (left < size ? heap[left] > heap[largest] : false) {
		largest = left;
	}
	if (right < size ? heap[right] > heap[largest] : false) {
		largest = right;
	}
	if (largest != index) {
		swap(heap[index], heap[largest]);
		sift_down(largest);
	}
}

template <typename T>
void	Heap<T>::sift_up(int index) {
	int parent = (index - 1) / 2;
	int least = index;
	if (parent >= 0 ? heap[least] > heap[parent] : false) {
		least = parent;
	}
	if (least != index) {
		swap(heap[least], heap[index]);
		sift_up(least);
	}
}

template <typename T>
void	Heap<T>::increase_dec() {
	T *buffer = new T[buf_size * 2];
	for (int i = 0; i < size; i++) {
		buffer[i] = heap[i];
	}
	delete[] heap;
	heap = buffer;
	buf_size *= 2;
}

template <typename T>
void	Heap<T>::decrease_dec() {
	T		*buffer = new T[buf_size / 2];
	for (int i = 0; i < size; i++) {
		buffer[i] = heap[i];
	}
	delete[] heap;
	heap = buffer;
	buf_size /= 2;
}

template <typename T>
T		Heap<T>::get(int index) {
	assert(!empty() & (index < size));
	return heap[index];
}

template <typename T>
T		Heap<T>::pop(int index) {
	assert(!empty() & (index < size));
	if (size > 0 && size < buf_size / 4 ) {
		decrease_dec();
	}
	T	tempData = heap[index];
	size--;
	if (size > 0) {
		swap(heap[index], heap[size]);
		sift_down(index);
	}
	return tempData;
}

template <typename T>
void	Heap<T>::push(T data) {
	if (size == buf_size) {
		increase_dec();
	}
	heap[size] = data;
	if (size > 0) {
		sift_up(size);
	}
	size++;
}

struct Train {
	int arrival;
	int departure;
	Train() {};
	bool operator >(const Train& x) {
		if (departure < x.departure)
			return true;
		if (departure == x.departure)
			return arrival < x.arrival;
		return false;
	}
	bool operator <(const Train& x) {
		if (departure > x.departure)
			return true;
		if (departure == x.departure)
			return arrival > x.arrival;
		return false;
	}
};

int		main() {
	int n;
	cin >> n;
	Train *timetable = new Train[1];
	cin >> timetable[0].arrival >> timetable[0].departure;
	
	Heap<Train> heap(1, timetable);
	int platform = 1;
	for (int i = 1; i < n; i++) {
		Train temp;
		cin >> temp.arrival >> temp.departure;
		if (heap.size > 0 ? heap.get(0).departure < temp.arrival : false) {
			heap.pop(0);
		}
		heap.push(temp);
		platform = heap.size > platform ? heap.size : platform;
	}
	cout << platform;
	return 0;
}
