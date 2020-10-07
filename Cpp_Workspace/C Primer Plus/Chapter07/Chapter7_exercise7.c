#include <stdio.h>
#define BASE_SALARY 10
#define BASE_WORK 40
#define OVERTIME_MULTIPLE 1.5
#define TAX_BASE_LEVEL1 300
#define TAX_RATE_LEVEL1 0.15
#define TAX_BASE_LEVEL2 450
#define TAX_RATE_LEVEL2 0.2
#define TAX_RATE_LEVEL3 0.25

int main(void)
{
    float work_hours;
    float salary;
    float tax;
    float net_income;
    printf("Enter total work hours:");
    scanf("%f", &work_hours);
    if (work_hours > 40)
    {
        work_hours = BASE_WORK + OVERTIME_MULTIPLE * (work_hours - BASE_WORK);
    }
    salary = work_hours * BASE_SALARY;
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

    return 0;
}