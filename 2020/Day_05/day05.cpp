#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int PartOne(){
    fstream file;
    file.open("input.txt");
    string text, letter;
    int l1 = 0, r1 = 127, l2 = 0, r2 = 7, row, col, ID, max = 0;

    while (file >> text){
        l1 = 0;
        r1 = 127;
        l2 = 0;
        r2 = 7;
        for (int i = 0; i < 6; i++){
            letter = text.substr(i, 1);
            if (letter == "F"){
                r1 = (l1 + r1) / 2;
            }
            else{
                l1 = ((l1 + r1) / 2) + 1;
            }
        }

        letter = text.substr(6, 1);
        if (letter == "F"){
            row = l1;
        } else{
            row = r1;
        }

        for (int i = 7; i < 9; i++){
            letter = text.substr(i, 1);
            if (letter == "L"){
                r2 = (l2 + r2) / 2;
            }
            else{
                l2 = ((l2 + r2) / 2) + 1;
            }
        }

        letter = text.substr(9, 1);
        if (letter == "L"){
            col = l2;
        } else{
            col = r2;
        }

        ID = (row * 8) + col;
        if (ID > max){
            max = ID;
        }
    }
    return max;
}

int PartTwo(){
    fstream file;
    file.open("input.txt");
    string text, letter;
    int l1 = 0, r1 = 127, l2 = 0, r2 = 7, row, col, ID, tab[128][8] = {0};

    while (file >> text){
        l1 = 0;
        r1 = 127;
        l2 = 0;
        r2 = 7;
        for (int i = 0; i < 6; i++){
            letter = text.substr(i, 1);
            if (letter == "F"){
                r1 = (l1 + r1) / 2;
            }
            else{
                l1 = ((l1 + r1) / 2) + 1;
            }
        }

        letter = text.substr(6, 1);
        if (letter == "F"){
            row = l1;
        } else{
            row = r1;
        }

        for (int i = 7; i < 9; i++){
            letter = text.substr(i, 1);
            if (letter == "L"){
                r2 = (l2 + r2) / 2;
            }
            else{
                l2 = ((l2 + r2) / 2) + 1;
            }
        }

        letter = text.substr(9, 1);
        if (letter == "L"){
            col = l2;
        } else{
            col = r2;
        }

        tab[row][col] = 1;
    }

    for (int i = 3; i < 100; i++){
        for (int j = 0; j < 8; j++){
            if (tab[i][j] == 0){
                return (i * 8) + j;
            }
        }
    }
    return 0;
}

int main(){

    cout << PartOne() << endl;
    cout << PartTwo() << endl;

    return 1;
}