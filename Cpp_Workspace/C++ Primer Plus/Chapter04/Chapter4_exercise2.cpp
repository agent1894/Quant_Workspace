// 4.13.2 -- ask grades using string
#include <iostream>
#include <string>
#include <cstring>

int main()
{
    using namespace std;

    string firstName;
    string lastName;
    char grade;
    int age;

    cout << "What is your first name? ";
    getline(cin, firstName);
    cout << "What is your last name? ";
    getline(cin, lastName);
    cout << "What letter grade do you deserve? ";
    cin >> grade;
    cout << "What is your age? ";
    cin >> age;
    grade = grade + 1;
    cout << "Name: " << lastName << ", " << firstName << endl;
    cout << "Grade: " << grade << endl;
    cout << "Age: " << age << endl;

    return 0;
}