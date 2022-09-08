#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct code{
    int id;
    string operation;
    int arg;
};

void PartOne(){
    fstream file;
    file.open("input.txt");

    vector<code> Codes;
    string line;
    vector<string> data;

    while(getline(file, line)){
        data.push_back(line);
    }

    for (int i = 0; i < data.size(); i++){

    }
}

int main(){

    PartOne();

    return 1;
}