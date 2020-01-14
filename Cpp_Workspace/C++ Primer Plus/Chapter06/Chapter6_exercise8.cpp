// 6.11.8 -- read and count characters
#include <iostream>
#include <fstream>
#include <cstdlib>

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
    int count = 0;
    char ch;
    inFile >> ch;
    while (inFile >> ch) // while input good and not at EOF
        ++count; // one more item read
    if (inFile.eof())
        cout << "End of file reached." << endl;
    else
        cout << "Input terminated for unknown reason. " << endl;
    cout << "The file has " << count << " characters." << endl;
    inFile.close();

    return 0;
}