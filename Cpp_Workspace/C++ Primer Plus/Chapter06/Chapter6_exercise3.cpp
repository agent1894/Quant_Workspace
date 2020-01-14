// 6.11.3 -- prototype of a menu drive program
#include <iostream>

int main()
{
    using namespace std;
    cout << "Please enter the following choices: " << endl;
    cout << "c) carnivore      p) pianist" << endl;
    cout << "t) tree           g) game" << endl;
    char choice;
    cin >> choice;
    while (choice != 'c' && choice != 'p' && choice != 't' && choice != 'g')
    {
        cout << "Please enter a c, p, t, or g: ";
        cin >> choice;
    }
    switch (choice)
    {
        case 'c' : cout << "A tiger is a carnivore." << endl;
            break;
        case 'p' : cout << "Franz Liszt is a pianist." << endl;
            break;
        case 't' : cout << "A maple is a tree." << endl;
            break;
        default : cout << "Assassin's Creed is a game." << endl;
            break;
    }

    return 0;
}