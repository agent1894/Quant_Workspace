// 4.13.1 -- ask grades
#include <iostream>

int main()
{
    using namespace std;

    char firstName[30];
    char lastName[30];
    char grade;
    int age;

    cout << "What is your first name? ";
    cin.getline(firstName, 30);
    cout << "What is your last name? ";
    cin.getline(lastName, 30);
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