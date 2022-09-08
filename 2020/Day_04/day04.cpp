#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int PartOne(){
    fstream file;
    file.open("input.txt");
    string text;

    string search[7] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};


    int pos, searchSum = 0, sum = 0;
    while(getline(file, text)){
        if(text == ""){
            if (searchSum == 7){
                sum++;
            }
                searchSum = 0;
        } else {

            for (int i = 0; i < 7; i++) {
                pos = 0;
                while ((pos = text.find(search[i], pos)) != string::npos){
                    searchSum++;
                    pos += search[i].length();
                }
            }
        }
    }
    if(searchSum == 7) {
        sum++;
    }
    return sum;
}

int PartTwo(){
    fstream file;
    file.open("input.txt");
    string text, text2;
    int pos = 0, searchSum = 0, sum = 0, date, height;

    string search[7] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
    string color[7] = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};

    while(getline(file, text)){
        if(text == ""){
            if (searchSum == 7){
                sum++;
            }
                searchSum = 0;
        }
        else {

            for (int i = 0; i < 7; i++) {
                pos = 0;
                while ((pos = text.find(search[i], pos)) != string::npos){
                    switch(i){
                        case 1:
                            date = atoi(text.substr(pos+4).c_str());
                            if (date >= 1920 && date <= 2002){
                                searchSum++;
                            }
                            break;
                        case 2:
                            date = atoi(text.substr(pos+4).c_str());
                            if (date >= 2010 && date <= 2020){
                                searchSum++;
                            }
                            break;
                        case 3:
                            date = atoi(text.substr(pos+4).c_str());
                            if (date >= 2020 && date <= 2030){
                                searchSum++;
                            }
                            break;
                        case 4:
                            text2 = text;
                            if(text2.substr(pos + 6) == "in"){
                                height = atoi(text.substr(pos+4).c_str());
                                if (height >= 59 && height <= 76){
                                    searchSum++;
                                }
                            }
                            else if(text2.substr(pos + 7) == "cm"){
                                height = atoi(text.substr(pos+4).c_str());
                                if (height >= 150 && height <= 193){
                                    searchSum++;
                                }
                            }
                            break;
                        case 5:
                            cout<<text[pos+4]<<endl;
                            if (text[pos+4] == '#'){
                                for (int j = 5; j < 11; j++){
                                    if(!isdigit(text[pos+i] || !isalpha(text[pos+i]))) {
                                        break;
                                    }
                                }
                                searchSum++;
                            } else {break;}
                            break;
                        case 6:
                            text2 = text.substr(pos + 4);
                            for (int j = 0; j < 7; j++){
                                if(text2 == color[i]){
                                    searchSum++;
                                    break;
                                }
                            }
                            break;
                        case 7:
                            if (text.substr(pos + 4).length() == 9){
                                for (int j = 4; j < 13; j++){
                                    if(!isdigit(text[pos+i])) {
                                        break;
                                    }
                                }
                                searchSum++;
                                break;
                            }
                            break;
                    }
                    pos += search[i].length();
                    // cout << text << endl;
                }
            }
        }

    }
    return sum;
}

int main(){

    cout << PartOne() << endl;
    cout << PartTwo() << endl;

    return 0;
}