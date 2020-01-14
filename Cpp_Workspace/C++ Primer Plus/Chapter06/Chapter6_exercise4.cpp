// 6.11.4 -- Benevolent Order of Program
#include <iostream>

const int StrSize = 80;

struct bop
{
    char fullName[StrSize]; // real name
    char title[StrSize]; // job title
    char bopname[StrSize]; // secret BOP name
    int perference; // 0 = fullname, 1 = title, 2 = bopname
};

int main()
{
    using namespace std;
    const int TeamMember = 5;
    bop team[TeamMember] = 
    {
        {"Wimp Macho", "Director", "IMP", 0},
        {"Raki Rhodes", "Junior Programmer", "IKAR", 1},
        {"Celia Laiter", "Senior Programmer", "MIPS", 2},
        {"Hoppy Hipman", "Analyst Trainee", "PIP", 1},
        {"Pat Hand", "Analyst", "LOOPY", 2}
    };

    cout << "Benevolent Order of Programmers Report" << endl;
    cout << "a. display by name     b. display by title" << endl;
    cout << "c. display by bopname  d. display by preference" << endl;
    cout << "q. quit" << endl;
    cout << "Enter your choice: ";
    char choice;
    cin >> choice;
    while (choice != 'q')
    {
        for (int i = 0; i < TeamMember; ++i)
        {
            switch (choice)
            {
                case 'a' :
                    cout << team[i].fullName << endl;
                    break;
                case 'b' :
                    cout << team[i].title << endl;
                    break;
                case 'c' :
                    cout << team[i].bopname << endl;
                    break;
                default : 
                    switch (team[i].perference)
                    {
                        case 0 : 
                            cout << team[i].fullName << endl;
                            break;
                        case 1 :
                            cout << team[i].title << endl;
                            break;
                        default :
                              cout << team[i].bopname << endl;
                    }
            }
        }
        cout << "Next choice: ";
        cin >> choice;
    }
    cout << "Bye!" << endl;

    return 0;
}