#include <stdio.h>

int main(void)
{
    double mass_mol = 3.0e-23;
    double mass_qt = 950;
    double water_qt;
    printf("Enter the quarts of water: ");
    scanf("%lf", &water_qt);
    printf("The %lf water has %e mol of molecules\n", water_qt, water_qt * mass_qt / mass_mol);

    return 0;
}