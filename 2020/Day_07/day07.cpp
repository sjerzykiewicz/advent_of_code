#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int PartOne(){
    fstream file;
    file.open("input.txt");
    string text;

    vector<string> bags;
    bags.push_back("shiny gold");
    int sum = 0, i = 0;
    cout << bags[i] << endl;

    // while(getline(file, text)){
    //     if (text.find(bags[i]) != std::string::npos) {
    //         int index = 0;
    //         for (int i = 0; i < 2; ++i){
    //             index = (text.find(" ", index)) + 1;
    //         }
    //         bags.push_back(text.substr(0, index));
    //         sum++;
    //     }
    // }

    // for(int i = 0; i < bags.size(); i++){
    //     cout << bags[i] << endl;
    // }

    return sum;

}

int main(){
    PartOne();
    return 1;
}