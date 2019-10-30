// 7.13.2 -- gold scores
#include <iostream>
using namespace std;
const int Max = 10;
int fillScore(double arr[], int limit);
void showScore(double arr[], int n);
double calAverage(double arr[], int n);

int main()
{
    double arr[Max];
    int n;
    n = fillScore(arr, Max);
    showScore(arr, n);
    cout << "The average score is: " << calAverage(arr, n) << endl;
    cout << "Done!" << endl;

    return 0;
}

int fillScore(double arr[], int limit)
{
    cout << "Please enter at most " << limit << " golf scores: " << endl;
    int i;
    for (i = 0; i < limit; i++)
    {
        cout << "Enter the score #" << i + 1 <<": ";
        double temp;
        if (!(cin >> temp) || temp < 0)
        {
            cout << "Bad input, program terminated." << endl;
            break;
        }
        else
            arr[i] = temp;
    }

    return i;
} 

void showScore(double arr[], int n)
{
    cout << "The scores are: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << '\t';
    cout << endl;
}

double calAverage(double arr[], int n)
{
    double sum = 0.0;
    for (int i = 0; i < n; i++)
        sum += arr[i];
    
    return sum / n;
}