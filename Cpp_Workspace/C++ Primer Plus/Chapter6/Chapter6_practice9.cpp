// 6.11.9 -- rewrite of pracite 6.11.6 by reading data from file
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>

struct patron
{
    std::string name;
    double money;
};

int main()
{
    using namespace std;
    cout << "Enter the file name: ";
    string filename;
    cin >> filename;
    ifstream inFile;
    inFile.open(filename);
    if (!inFile.is_open()) // failed to open file
    {
        cout << "Could not open the file " << filename << endl;
        cout << "Program terminating. " << endl;
        exit(EXIT_FAILURE);
    }
    int number;
    inFile >> number;
    inFile.get();
    patron * patrons = new patron[number];
    for (int i = 0; i < number; ++i)
    {
        getline(inFile, patrons[i].name);
        inFile >> patrons[i].money;
        inFile.get();
    }
    if (inFile.eof())
        cout << "End of file reached." << endl;
    else
        cout << "Input terminated for unknown reason. " << endl;
    cout << "Grand Patrons: " << endl;
    int count = 0;
    for (int i = 0; i < number; ++i)
    {
        if (patrons[i].money >= 10000)
        {
            cout << patrons[i].name << ": $" << patrons[i].money << '\t';
            ++count;
        }
    }
    if (count == 0)
        cout << "None" << endl;
    else
        cout << endl;
    cout << "Patrons: " << endl;
    count = 0;
    for (int i = 0; i < number; ++i)
    {
        if (patrons[i].money < 10000)
        {
            cout << patrons[i].name << '\t';
            ++count;
        }
    }
    if (count == 0)
        cout << "None" << endl;
    else
        cout << endl;

    delete [] patrons;
    
    return 0;
}