#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		char* p = (char*)malloc(sizeof(char) * (100001));
		scanf("%s", p);
		int len = strlen(p);
		
		int dCnt = 0;
		for (int j = 0; j < len; j++)
			if (p[j] == 'D')
				dCnt++;
		

		int n;
		scanf("%d", &n);

		int* arr = (int*)malloc(sizeof(int) * n);
		getchar();
		getchar();
		for (int j = 0; j < n; j++) {
			scanf("%d", &arr[j]);
			getchar();
		}
		if (n == 0)
			getchar();
		
		if (dCnt > n) {
			printf("error\n");
			getchar();
			continue;
		}
		

		int state = 0;
		int a = 0;
		int b = n - 1;
		for (int j = 0; j < len; j++) {
			if (p[j] == 'R')
				state++;
			else {
				if (state % 2 == 0)
					a++;
				else
					b--;
				n--;
			}
		}


		/* O(n) => 출력 거꾸로 조지기
		if (state % 2 == 1) {
			for (int j = 0; j < n / 2; j++) {
				int tmp = arr[j];
				arr[j] = arr[n - 1 - j];
				arr[n - 1 - j] = tmp;
			}
		}
		*/
		if (n == 0)
			printf("[]\n");
		else {
			if (state % 2 == 0) {
				printf("[%d", arr[a]);
				for (int j = a+1; j <= b; j++) {
					printf(",%d", arr[j]);
				}
				printf("]\n");
			}
			else {
				printf("[%d", arr[b]);
				for (int j = b-1; j >= a; j--)
					printf(",%d", arr[j]);
				printf("]\n");
			}
		}

	}

	return 0;
}