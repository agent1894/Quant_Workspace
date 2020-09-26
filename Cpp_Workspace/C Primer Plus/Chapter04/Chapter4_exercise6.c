#include <stdio.h>
#include <string.h>

int main(void)
{
    char first_name [20];
    char last_name [20];
    int fname_len;
    int lname_len;
    printf("Enter first name: ");
    scanf("%s", first_name);
    printf("Enter last name: ");
    scanf("%s", last_name);
    fname_len = strlen(first_name);
    lname_len = strlen(last_name);
    printf("%s %s\n", first_name, last_name);
    printf("%*d %*d\n", fname_len, fname_len, lname_len, lname_len);
    printf("%s %s\n", first_name, last_name);
    printf("%-*d %-*d\n", fname_len, fname_len, lname_len, lname_len);
    
    return 0;
}