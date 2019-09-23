// 3.7.5 -- population
#include <iostream>
#include <climits>

int main()
{
    using namespace std;
    long long world_population, region_population;
    cout << "Enter the world's population: ";
    cin >> world_population;
    cout << "Enter the population of the US: ";
    cin >> region_population;
    double percent = 100.0 * region_population / world_population;
    cout << "The population of the US is ";
    cout << percent << "% of the wrold population." << endl;

    return 0;
}