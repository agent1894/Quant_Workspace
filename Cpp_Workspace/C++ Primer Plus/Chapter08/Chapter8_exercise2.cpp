// 8.8.2 -- CandyBar structure
#include <iostream>
#include <string>
using namespace std;

struct CandyBar
{
    const char* brand;
    double weight;
    long carlore;
};

void fill(CandyBar& candy, const char* brand = "Millennium Munch", double weight = 2.85, long carlore = 350);
void show(const CandyBar& candy);

int main()
{
    CandyBar candy;
    fill(candy);
    show(candy);

    cout << "Please enter the brand: ";
    const int Len = 80;
    char brand[Len];
    cin.getline(brand, Len);
    cout << "Please enter the weight: ";
    double weight;
    cin >> weight;
    cout << "Please enter the carlore: ";
    long carlore;
    cin >> carlore;
    fill(candy, brand, weight, carlore);
    show(candy);

    return 0;
}

void fill(CandyBar& candy, const char* brand, double weight, long carlore)
{
    candy.brand = brand;
    candy.weight = weight;
    candy.carlore = carlore;
}

void show(const CandyBar& candy)
{
    cout << "The brand of the CandyBar is: " << candy.brand << endl;
    cout << "The weight of the CandyBar is: " << candy.weight << endl;
    cout << "The carlore of the CandyBar is: " << candy.carlore << endl;
}