#include <iostream>
#include <fstream>

using namespace std;

int calcTrees(char tab[323][31], int down, int right){
    int sumTrees = 0;
    int j = 0;
    for(int i = 0; i < 323; i += down){
        if (tab[i][j] == '#'){
            sumTrees++;
        }
        j += right;
        if (j > 30){
            j %= 30;
            j--;
        }
    }

    return sumTrees;
}

int PartOne(){
    fstream file;
    file.open("input.txt");

    char board[323][31];
    for(int i = 0; i < 323; i++){
        for(int j = 0; j < 31; j++){
            file >> board[i][j];
        }
    }
    return calcTrees(board, 1, 3);
}

int PartTwo(){
    fstream file;
    file.open("input.txt");

    char board[323][31];
    for(int i = 0; i < 323; i++){
        for(int j = 0; j < 31; j++){
            file >> board[i][j];
        }
    }
    return (calcTrees(board, 1, 1) * calcTrees(board, 1, 3) * calcTrees(board, 1, 5) * calcTrees(board, 1, 7) * calcTrees(board, 2, 1));
}



int main(){

    cout << PartOne() << endl;
    cout << PartTwo() << endl;

    return 0;
}