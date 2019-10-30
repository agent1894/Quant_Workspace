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
void setBox(box newBox);
void showBox(box newBox);

int main()
{
    using namespace std;
    box newBox = {"MakerA", 10.0, 10.0, 10.0, 100.0};
    showBox(newBox);

    return 0;
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

void 