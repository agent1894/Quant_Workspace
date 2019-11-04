// 7.13.6 -- array reversing
#include <iostream>
int Fill_array(double arr[], int limit);
void Show_array(const double arr[], int n);
void Reverse_array(double arr[], int n);

int main()
{
    using namespace std;
    cout << "Enter the number of doubles you want to save: ";
    int limit;
    cin >> limit;
    double arr[limit];
    int n = Fill_array(arr, limit);
    Show_array(arr, n);
    cout << "After reverse the whole array..." << endl;
    Reverse_array(arr, n);
    Show_array(arr, n);
    cout << "After reverse the array between the first element and the last element..." << endl;
    Reverse_array(arr + 1, n - 2);
    Show_array(arr, n);

    return 0;
}

int Fill_array(double arr[], int limit)
{
    using namespace std;
    int i;
    for (i = 0; i < limit; i++)
    {
        cout << "Enter the #" << i + 1 << ": ";
        double tmp;
        if (cin >> tmp)
            arr[i] = tmp;
        else
            break;
    }
    cout << "There are " << i << " inputs in total." << endl;

    return i;
}

void Show_array(const double arr[], int n)
{
    using namespace std;
    cout << "Now show the array: " << endl;
    for (int i = 0; i < n ; i++)
        cout << "The input #" << i + 1 << ": " << arr[i] << endl;
}

void Reverse_array(double arr[], int n)
{
    int i, j;
    for (i = 0, j = n - 1; i < j; i++, j--)
    {
        double tmp;
        tmp = arr[j];
        arr[j] = arr[i];
        arr[i] = tmp;
    }
}