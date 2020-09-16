#include <iostream>
#include <string>

using namespace std;

struct Position {
	char h;
	int w;
	Position(char height, int weight) :
	h(height),
	w(weight) {}
};

bool operator != (Position &p1, Position &p2) {
	return (p1.h != p2.h or p1.w != p2.w);
}

bool operator == (Position &p1, Position &p2) {
	return (p1.h == p2.h and p1.w == p2.w);
}

bool attack_king(Position b_king, Position w_king) {
	if (b_king.h >= w_king.h - 1 and b_king.h <= w_king.h + 1) {
		if (b_king.w >= w_king.w - 1 and b_king.w <= w_king.w + 1) {
			return true;
		}
	}
	return false;
}

template <typename T>
bool between(T a, T b, T c) {
	if (c > (a < b ? a : b)) {
		if (c < (a > b ? a : b)) {
			return true;
		}
	}
	return false;
}

bool attack_rook(Position b_king, Position w_king, Position w_rook) {
	if (b_king == w_rook) {
		return false;
	}
	if (b_king.h == w_rook.h) {
		if (!(w_king.h == b_king.h and between(b_king.w, w_rook.w, w_king.w))) {
			return true;
		}
	}
	if (b_king.w == w_rook.w) {
		if (!(w_king.w == b_king.w and between(b_king.h, w_rook.h, w_king.h))) {
			return true;
		}
	}
	return false;
}

bool next_step(Position b_king, Position w_king, Position w_rook) {
	for (char h = b_king.h - 1; h <= b_king.h + 1; h++) {
		for (int w = b_king.w - 1; w <= b_king.w + 1; w++) {
			if (h >= 'a' and h <= 'h' and w >= 1 and w <= 8) {
				if (!(b_king.h == h and b_king.w == w)) {
					if (!attack_king(Position(h, w), w_king) and !attack_rook(Position(h, w), w_king, w_rook)) {
						return true;
					}
				}
			}
		}
	}
	return false;
}

int main() {
	string w_k, w_r, b_k;
	cin >> w_k >> w_r >> b_k;
	
	Position w_king(w_k[0], w_k[1] - '0');
	Position w_rook(w_r[0], w_r[1] - '0');
	Position b_king(b_k[0], b_k[1] - '0');
	
	if (attack_king(b_king, w_king)) {
		cout << "Strange";
	} else if (attack_rook(b_king, w_king, w_rook)) {
		if (next_step(b_king, w_king, w_rook)) {
			cout << "Check";
		} else {
			cout << "Checkmate";
		}
	} else {
		if (next_step(b_king, w_king, w_rook)) {
			cout << "Normal";
		} else {
			cout << "Stalemate";
		}
	}
    return 0;
}
