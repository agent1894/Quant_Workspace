// 4.13.8 -- William Wingate Pizza using new
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

    Pizza * pt = new Pizza;
    cout << "Enter the company name of pizza: ";
    getline(cin, pt->company);
    cout << "Enter the diameter of pizza: ";
    cin >> pt->diameter;
    cout << "Enter the weight of pizza: ";
    cin >> pt->weight;

    cout << "The company of the pizza is: " << (*pt).company << endl;
    cout << "The diameter of the pizza is: " << (*pt).diameter << " inches";
    cout << ", and the weight of the pizza is: " << (*pt).weight << " grams" << endl;

    delete pt;

    return 0;
}