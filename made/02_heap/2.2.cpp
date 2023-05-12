#include <assert.h>
#include <iostream>

using namespace std;

template <typename T>
class Heap {
public:
	Heap(size_t size, T* elements);
	size_t	size;
	T		get(size_t index);
	T		pop(size_t index);
	void	push(T data);
private:
	size_t	buf_size;
	T*		heap;
	bool	empty();
	void	build_heap();
	void	sift_down(size_t index);
	void	sift_up(size_t index);
	void	increase_dec();
	void	decrease_dec();
};

template <typename T>
Heap<T>::Heap(size_t size, T* elements) :
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
	for (size_t i = size / 2 + 1 ; i > 0 ; i--) {
		sift_down(i - 1);
	}
}

template <typename T>
void	Heap<T>::sift_down(size_t index) {
	size_t left = 2 * index + 1;
	size_t right = 2 * index + 2;
	size_t largest = index;
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
void	Heap<T>::sift_up(size_t index) {
	size_t parent = (index - 1) / 2;
	size_t least = index;
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
	for (size_t i = 0; i < size; i++) {
		buffer[i] = heap[i];
	}
	delete[] heap;
	heap = buffer;
	buf_size *= 2;
}

template <typename T>
void	Heap<T>::decrease_dec() {
	T		*buffer = new T[buf_size / 2];
	size_t	h_size = size;
	for (size_t i = 0; i < h_size; i++) {
		buffer[i] = heap[i];
	}
	delete[] heap;
	heap = buffer;
	buf_size /= 2;
}

template <typename T>
T		Heap<T>::get(size_t index) {
	assert(!empty() & (index < size));
	return heap[index];
}

template <typename T>
T		Heap<T>::pop(size_t index) {
	assert(!empty() & (index < size));
	if (size < buf_size / 4 ) {
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

int		main() {
	int n;
	cin >> n;
	int* num = new int[n];
	for (size_t i = 0; i < n; i++) {
		cin >> num[i];
		num[i] *= -1;
	}

	Heap<int> heap(n, num);
	long long ans = 0;
	while (heap.size > 0) {
		int sum = -heap.pop(0);
		if (heap.size > 0)
		{
			sum -= heap.pop(0);
			ans += sum;
			heap.push(-sum);
		}
	}
	cout << ans << endl;
	return 0;
}
