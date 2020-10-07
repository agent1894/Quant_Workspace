#include <stdio.h>
#include <ctype.h>

int main(void)
{
    const float ARTICHOKE_PRICE = 2.05;
    const float SUGARBEET_PRICE = 1.15;
    const float CARROT_PRICE = 1.09;
    const float DISCOUNT_RATE = 0.05;
    float total_pounds = 0;
    float temp_pounds = 0;
    float artichoke_pounds = 0;
    float sugarbeet_pounds = 0;
    float carrot_pounds = 0;
    float order_value = 0;
    float discount = 0;
    float dispatch_fees = 0;
    char type;

    printf("Enter type for recording order pounds:\nA for artichoke, S for sugarbeet, C for carrot and Q for quit.\n");
    type = getchar();
    type = toupper(type);
    while (type != 'Q')
    {
        switch (type)
        {
        case 'A':
            printf("Enter pounds for artichoke: ");
            scanf("%f", &temp_pounds);
            printf("\n");
            artichoke_pounds += temp_pounds;
            break;

        case 'S':
            printf("Enter pounds for sugarbeet: ");
            scanf("%f", &temp_pounds);
            printf("\n");
            sugarbeet_pounds += temp_pounds;
            break;

        case 'C':
            printf("Enter pounds for carrot: ");
            scanf("%f", &temp_pounds);
            printf("\n");
            carrot_pounds += temp_pounds;
            break;

        case 'Q':
            printf("Quit order.\n");
            break;
        
        default:
            printf("A for artichoke, S for sugarbeet, C for carrot and Q for quit.\n");
            break;
        }
        type = getchar();
        type = toupper(type);
    }
    total_pounds = artichoke_pounds + sugarbeet_pounds + carrot_pounds;
    order_value = artichoke_pounds * ARTICHOKE_PRICE + sugarbeet_pounds * SUGARBEET_PRICE + carrot_pounds * CARROT_PRICE;
    if (order_value >= 100)
    {
        discount = order_value * DISCOUNT_RATE;
    }
    if (total_pounds <= 5)
    {
        dispatch_fees = 6.5;
    }
    else if (5 < total_pounds && total_pounds <= 20)
    {
        dispatch_fees = 14;
    }
    else
    {
        dispatch_fees = 14 + 0.5 * (total_pounds - 14);
    }
    
    printf("********************Order Details********************\n");
    printf("Artichoke is $%.2f/pounds, total %.2f pounds with $%.2f.\n", ARTICHOKE_PRICE, artichoke_pounds, ARTICHOKE_PRICE * artichoke_pounds);
    printf("Sugarbeet is $%.2f/pounds, total %.2f pounds with $%.2f.\n", SUGARBEET_PRICE, sugarbeet_pounds, SUGARBEET_PRICE * sugarbeet_pounds);
    printf("Carrot is $%.2f/pounds, total %.2f pounds with $%.2f.\n", CARROT_PRICE, carrot_pounds, CARROT_PRICE * carrot_pounds);
    printf("********************Order Summary********************\n");
    printf("Total pounds of order is %.2f pounds, value of order is $%.2f, discount is $%.2f, dispatch and packing fees is $%.2f.\n", total_pounds, order_value, discount, dispatch_fees);
    printf("Final Order is $%.2f\n", order_value - discount + dispatch_fees);


    return 0;
}