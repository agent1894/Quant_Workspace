#include <stdio.h>
void Temperatures(double tempearture);

int main(void)
{
    double temperature;
    int q;
    printf("Enter temperature in F: ");
    q = scanf("%lf", &temperature);
    while (q == 1)
    {
        Temperatures(temperature);
        printf("Enter temperature in F (q to quit): ");
        q = scanf("%lf", &temperature);
    }
    printf("Done\n");

    return 0;
}

void Temperatures(double temperature)
{
    const double F_TO_C = 5.0 / 9.0;
    const double C_TO_K = 273.16;
    double temperature_C = F_TO_C * (temperature - 32.0);
    double temperature_K = C_TO_K + temperature_C;
    printf("Temperature is %.2fF, %.2fC, %.2fK\n", temperature, temperature_C, temperature_K);
}