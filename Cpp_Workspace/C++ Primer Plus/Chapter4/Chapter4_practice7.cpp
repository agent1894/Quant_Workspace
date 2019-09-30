// 4.13.7 -- William Wingate Pizza
#include <iostream>
#include <string>

struct Pizza
{
    std::string company;
    double diameter;
    double weight;
};

int main()
{
    using namespace std;

    Pizza pizza;
    cout << "Enter the company name of pizza: ";
    getline(cin, pizza.company);
    cout << "Enter the diameter of pizza: ";
    cin >> pizza.diameter;
    cout << "Enter the weight of pizza: ";
    cin >> pizza.weight;

    cout << "The company of the pizza is: " << pizza.company << endl;
    cout << "The diameter of the pizza is: " << pizza.diameter << " inches";
    cout << ", and the weight of the pizza is: " << pizza.weight << " grams" << endl;

    return 0;
}