#include <stdio.h>
#include <string.h>

int main(void)
{
    char first_name[20];
    char last_name[20];
    int fname_len;
    int lname_len; 
    int margin;
    printf("Enter the first name: ");
    scanf("%s", first_name);
    fname_len = strlen(first_name);
    printf("Enter the last name: ");
    scanf("%s", last_name);
    lname_len = strlen(last_name);
    printf("The name is \"%s %s\"\n", first_name, last_name);
    margin = 20 - fname_len - lname_len;
    printf("The name is \"%*s %s\"\n", margin + fname_len - 1, first_name, last_name);
    printf("The name is \"%s %*s\"\n", first_name, 1 - margin - lname_len, last_name);

    return 0;
}