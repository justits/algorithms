#include <assert.h>
#include <iostream>

using namespace std;

struct Node {
	int value;
	int index;
};

class Heap {
public:
	Heap(int size, Node** elements);
	int		size;
	Node*	get(int index);
	Node*	pop(int index);
	void	push(Node* data);
private:
	int	buf_size;
	Node**		heap;
	bool	empty();
	void	build_heap();
	void	sift_down(int index);
	void	sift_up(int index);
	void	increase_dec();
	void	decrease_dec();
};

Heap::Heap(int size, Node** elements) :
size(size),
buf_size(size) {
	heap = new Node*[size];
	for (int i = 0; i < size; i++) {
		heap[i] = elements[i];
		heap[i]->index = i;
	}
	build_heap();
}

bool	Heap::empty() {
	return size == 0;
}

void	Heap::build_heap() {
	for (int i = size / 2 + 1 ; i > 0 ; i--) {
		sift_down(i - 1);
	}
}

void	Heap::sift_down(int index) {
	int left = 2 * index + 1;
	int right = 2 * index + 2;
	int largest = index;
	if (left < size ? heap[left]->value > heap[largest]->value : false) {
		largest = left;
	}
	if (right < size ? heap[right]->value > heap[largest]->value : false) {
		largest = right;
	}
	if (largest != index) {
		swap(heap[index], heap[largest]);
		heap[index]->index = index;
		heap[largest]->index = largest;
		sift_down(largest);
	}
}

void	Heap::sift_up(int index) {
	int parent = (index - 1) / 2;
	int least = index;
	if (parent >= 0 ? heap[least]->value > heap[parent]->value : false) {
		least = parent;
	}
	if (least != index) {
		swap(heap[least], heap[index]);
		heap[index]->index = index;
		heap[least]->index = least;
		sift_up(least);
	}
}

void	Heap::increase_dec() {
	Node** buffer = new Node*[buf_size * 2];
	for (int i = 0; i < size; i++) {
		buffer[i] = heap[i];
	}
	delete[] heap;
	heap = buffer;
	buf_size *= 2;
}

void	Heap::decrease_dec() {
	Node** buffer = new Node*[buf_size / 2];
	for (int i = 0; i < size; i++) {
		buffer[i] = heap[i];
	}
	delete[] heap;
	heap = buffer;
	buf_size /= 2;
}

Node*	Heap::get(int index) {
	assert(!empty() & (index < size));
	return heap[index];
}

Node*	Heap::pop(int index) {
	assert(!empty() & (index < size));
	if (size > 0 && size < buf_size / 4 ) {
		decrease_dec();
	}
	Node*	tempData = heap[index];
	size--;
	if (size > 0) {
		swap(heap[index], heap[size]);
		heap[index]->index = index;
		heap[size]->index = size;
		sift_down(index);
	}
	return tempData;
}

void	Heap::push(Node* data) {
	if (size == buf_size) {
		increase_dec();
	}
	heap[size] = data;
	heap[size]->index = size;
	if (size > 0) {
		sift_up(size);
	}
	size++;
}

int		main() {
	int n;
	cin >> n;
	Node **num = new Node*[n];
	for (int i = 0; i < n; i++) {
		Node* temp = new Node;
		cin >> temp->value;
		num[i] = temp;
	}
	int k;
	cin >> k;
	Heap heap(k, num);
	
	cout << heap.get(0)->value;
	for (int i = 0; i < n - k; i++) {
		heap.pop(num[i]->index);
		heap.push(num[i + k]);
		cout << " " << heap.get(0)->value;
	}
	return 0;
}
