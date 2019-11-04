// 7.13.7 -- rewrite the program 7.7, using pointer to note the end position,
// instead of using the returned input count
#include <iostream>

const int Max = 5;
double* fill_array(double ar[], int limit);
void show_array(const double ar[], double* end);
void revalue(double r, double ar[], double* end);

int main()
{
    using namespace std;
    double properties[Max];

    double* endPosition = fill_array(properties, Max);
    show_array(properties, endPosition);
    if (endPosition > 0)
    {
        cout << "Enter revaluation factor: ";
        double factor;
        while (!(cin >> factor)) // bad input
        {
            cin.clear();
            while (cin.get() != '\n')
                continue;
            cout << "Bad input; Please enter a number: ";
        }
        revalue(factor, properties, endPosition);
        show_array(properties, endPosition);
    }
    cout << "Done." << endl;
    cin.get();
    cin.get();

    return 0;
}

double* fill_array(double ar[], int limit)
{
    using namespace std;
    double temp;
    int i;
    for (i = 0; i < limit; i++) // Fix bug here: shouldn't declare int i = 0 in the for loop initialization
    {
        cout << "Enter value #" << (i + 1) << ": ";
        cin >> temp;
        if (!cin) // bad input
        {
            cin.clear();
            while (cin.get() != '\n')
                continue;
            cout << "Bad input; input process terminated. " << endl;
            break;
        }
        else if (temp < 0) // signal to terminate
            break;
        ar[i] = temp;
    }

    return &ar[i];
}

void show_array(const double ar[], double* end)
{
    using namespace std;
    const double* pt; // 指针const？指针地址的值const？指针地址存入的值const？
    int n;
    for (pt = &ar[0], n = 0; pt != end; pt++)
    {
        cout << "Property #" << (n + 1) << ": $";
        cout << *pt << endl;
    }
}

void revalue(double r, double ar[], double* end)
{
    double* pt;
    for (pt = &ar[0]; pt != end; pt++)
        *pt *= r;
}