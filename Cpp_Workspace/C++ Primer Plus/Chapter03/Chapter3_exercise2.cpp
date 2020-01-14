// 3.7.2 -- calcualte BMI
#include <iostream>
#include <cmath>

int main()
{
    using namespace std;
    const double InchConvert = 12.0;
    const double MeterConvert = 0.0254;
    const double KgConvert = 2.2;
    cout << "Enter your height by feet and inches: " << endl;
    int feet, inches;
    cout << "Feet: ";
    cin >> feet;
    cin.get();
    cout << "Inches: ";
    cin >> inches;
    cout << "You are " << feet * InchConvert + inches << " inches. ";
    double height = (feet * InchConvert + inches) * MeterConvert;
    cout << "Equals " << height << " meters." << endl;
    cout << "Enter your weight in pounds: ";
    double pounds;
    cin >> pounds;
    double weight = pounds / KgConvert;
    cout << "You are " << weight << " kilograms." << endl;
    double bmi = weight / pow(height, 2);
    cout << "Your BMI is " << bmi << endl;

    return 0;
}