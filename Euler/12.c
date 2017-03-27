#include <stdio.h>

int medicine(int num);

int main(void)
{
	int i=2, num=1;

	while(1)
	{
		if(medicine(num) >= 500){
			break;
		}
			
		num += i;
		i ++;
		printf("%d\n", num);
	}	
	printf("%d", num);
	
	return 1;
}

int medicine(int num)
{
	int count=0, i;
	
	for(i=1; i<num+1; i++){
		if(num%i == 0){
			count ++;
		}
			
	}
	return count;
}
