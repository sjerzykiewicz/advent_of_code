#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

void PartOne(){
    fstream file;
    file.open("input.txt");

    string range;
    string letter;
    string pass;
    int r1, r2, count;
    char l;
    int sum = 0;
    do {
        count = 0;
        file >> range;
        file >> letter;
        file >> pass;
        r1 = atoi(range.substr(0).c_str());
        r2 = atoi(range.substr(2).c_str());
        if (r2 < 0) r2 *= -1;
        l = letter.at(0);
        // cout << r1 << " " << r2 << " " << l << " " << pass << endl;
        for (int i = 0; i < pass.length(); i++){
            if (pass[i] == l)
            {
                count++;
            }
        }
        // cout << "count: " << count << endl;
        if (count >= r1 && count <= r2){
            sum++;
            // cout << "!" << endl;
        }
    } while (!file.eof());
    cout << sum << endl;
    file.close();
}

void PartTwo(){
    fstream file;
    file.open("input.txt");

    string range;
    string letter;
    string pass;
    int r1, r2;
    char l;
    int sum = 0;
    do {
        file >> range;
        file >> letter;
        file >> pass;

        r1 = atoi(range.substr(0).c_str());
        r2 = atoi(range.substr(2).c_str());

        if (r2 < 0) r2 *= -1;
        l = letter.at(0);

        if ((pass[r1-1] == l && pass[r2-1] != l) || (pass[r1-1] != l && pass[r2-1] == l)){
            sum++;
        }
    } while (!file.eof());
    cout << sum << endl;
    file.close();
}

int main(){
    PartOne();
    PartTwo();
    return 0;
}