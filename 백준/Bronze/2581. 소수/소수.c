#include <stdio.h>

int minority(int n) {
	if (n == 1)
		return 0;
	if (n == 2)
		return 1;
	else if (n % 2 == 0)
		return 0;

	int cnt = 0;
	for (int i = 2; i < n; i++) {
		if (n % i == 0)
			return 0;
	}

	return 1;
}

int main() {
	int M, N;
	scanf("%d %d", &M, &N);

	int sum = 0;
	int min = N;
	for (int i = M; i <= N; i++) {
		if (minority(i) == 1) {
			sum += i;
			if (min > i)
				min = i;
		}
	}

	if (sum == 0)
		printf("-1");
	else
		printf("%d\n%d", sum, min);

	return 0;
}