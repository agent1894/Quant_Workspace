// 7.13.3 -- structure functions
#include <iostream>
struct box
{
    char maker[40];
    float height;
    float weight;
    float length;
    float volume;
};
void initBox(box* ptBox);
void showBox(box newBox);

int main()
{
    using namespace std;
    box newBox; 
    initBox(&newBox);
    showBox(newBox);

    return 0;
}

void initBox(box* ptBox)
{
    using namespace std;
    cout << "Enter the box maker: ";
    cin.getline(ptBox->maker, 40);
    cout << "Enter the height: ";
    cin >> ptBox->height;
    cout << "Enter the weight: ";
    cin >> (*ptBox).weight;
    cout << "Enter the length: ";
    cin >> (*ptBox).length;
    ptBox->volume = (*ptBox).height * (*ptBox).weight * (*ptBox).length;
}

void showBox(box newBox)
{
    using namespace std;
    cout << "The box maker is: " << newBox.maker << endl;
    cout << "The box height is: " << newBox.height << endl;
    cout << "The box weight is: " << newBox.weight << endl;
    cout << "The box length is: " << newBox.length << endl;
    cout << "The box volume is: " << newBox.volume << endl;
}
