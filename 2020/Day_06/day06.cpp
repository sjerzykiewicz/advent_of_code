#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int PartOne(){
    fstream file;
    file.open("input.txt");
    string text;

    int tab[26] = {0}, groupSum = 0, sum = 0;

    while (getline(file, text)){
        if(text == ""){
            for (int i = 0; i < 26; i++){
                if (tab[i] == 1){
                    groupSum++;
                }
            }
            for (int i = 0; i < 26; i++){
                tab[i] = 0;
            }
            sum += groupSum;
            groupSum = 0;
        }
        else {
            for (int i = 0; i < text.length(); i++){
                tab[text[i] - 97] = 1;
            }
        }
    }
    for (int i = 0; i < 26; i++){
                if (tab[i] == 1){
                    groupSum++;
                }
            }
            for (int i = 0; i < 26; i++){
                tab[i] = 0;
            }
            sum += groupSum;
            groupSum = 0;

    return sum;
}

int PartTwo(){
    fstream file;
    file.open("input.txt");
    string text;

    int tab[26] = {0}, groupSum = 0, sum = 0, persons = 0;;

    while (getline(file, text)){
        if(text == ""){
            for (int i = 0; i < 26; i++){
                if (tab[i] == persons){
                    groupSum++;
                }
            }
            for (int i = 0; i < 26; i++){
                tab[i] = 0;
            }
            sum += groupSum;
            groupSum = 0;
            persons = 0;
        }
        else {
            persons++;
            for (int i = 0; i < text.length(); i++){
                tab[text[i] - 97] += 1;
            }
        }
    }
    for (int i = 0; i < 26; i++){
                if (tab[i] == persons){
                    groupSum++;
                }
            }
            for (int i = 0; i < 26; i++){
                tab[i] = 0;
            }
            sum += groupSum;
            groupSum = 0;

    return sum;
}

int main(){

    cout << PartOne() << endl;
    cout << PartTwo() << endl;

    return 1;
}