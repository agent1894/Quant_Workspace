#include <stdio.h>
#define BASE_WORK 40
#define OVERTIME_MULTIPLE 1.5
#define TAX_BASE_LEVEL1 300
#define TAX_RATE_LEVEL1 0.15
#define TAX_BASE_LEVEL2 450
#define TAX_RATE_LEVEL2 0.2
#define TAX_RATE_LEVEL3 0.25

int main(void)
{
    int choice;
    float payment_per_hour;
    float working_hours;
    float salary;
    float tax;
    float net_income;
    printf("********************\n");
    printf("Enter the number corresponding to the desired pay rate or action:\n");
    printf("1) $8.75/hr\t\t\t2) $9.33/hr\n3) $10.00/hr\t\t\t4) $11.20/hr\n5) quit\n");
    printf("********************\n");
    printf("Choice:");
    while (scanf("%d", &choice) == 1)
    {
        switch (choice)
        {
        case 1:
            payment_per_hour = 8.75;
            break;

        case 2:
            payment_per_hour = 9.33;
            break;

        case 3:
            payment_per_hour = 10.00;
            break;

        case 4:
            payment_per_hour = 11.20;
            break;

        case 5:
            printf("Done\n");
            return 0;
        
        default:
            printf("Please enter correct choice.\n");
            goto skip;
            break;
        }
        printf("Enter total working hours:");
        scanf("%f", &working_hours);
        if (working_hours > BASE_WORK)
        {
            working_hours = BASE_WORK + (working_hours - BASE_WORK) * OVERTIME_MULTIPLE;
        }
        salary = payment_per_hour * working_hours;
        if (salary > TAX_BASE_LEVEL1)
        {
            if (salary > TAX_BASE_LEVEL2)
            {
                tax = (salary - TAX_BASE_LEVEL2) * TAX_RATE_LEVEL3 + TAX_BASE_LEVEL1 * TAX_RATE_LEVEL1 + (TAX_BASE_LEVEL2 - TAX_RATE_LEVEL1) * TAX_RATE_LEVEL2;
            }
            else
            {
                tax = (salary - TAX_BASE_LEVEL1) * TAX_RATE_LEVEL2 + TAX_BASE_LEVEL1 * TAX_RATE_LEVEL1;
            }
            
        }
        else
        {
            tax = salary * TAX_RATE_LEVEL1;
        }
        net_income = salary - tax;

        printf("Salary before tax is %.2f, tax is %.2f, net income is %.2f\n", salary, tax, net_income);

    skip:
        printf("********************\n");
        printf("Enter the number corresponding to the desired pay rate or action:\n");
        printf("1) $8.75/hr\t\t\t2) $9.33/hr\n3) $10.00/hr\t\t\t4) $11.20/hr\n5) quit\n");
        printf("********************\n");
        printf("Choice:");
    }
}
    
