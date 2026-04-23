#include <stdio.h>
#include <string.h>
struct students
{
	char name[30];
	int  roll;
	float fees;
}s1 = {"denzel",10, 10.00}, s2;
int main()
{
	printf("\n############### lets display details for student1 ###################");
	printf("\n NAME \t ROLL \t FEES",s1.name,s1.roll,s1.fees);
	printf("\n %s \t %d \t %f",s1.name,s1.roll,s1.fees);
	strcpy(s2.name,"mancue");
	s2.roll = 11;
	s2.fees = 10.00;
	printf("\n %s \t %d \t %f",s2.name,s2.roll,s2.fees);
	return 0;
}