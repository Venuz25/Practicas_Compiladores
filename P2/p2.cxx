#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <regex>


using namespace std;

struct Lexema
{
    string token;
    string lexema;
    string valAtri;
};

int main(){
    ifstream archivo("Text.txt");
    if (!archivo)
    {
        cerr << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    vector<Lexema> lexemas;
    string palabra, linea;
    size_t position;

    cout << "TOKEN\t\t\t|\t\t\tLEXEMA\t\t\t|\t\t\tVALOR DE ATRIBUTO\n";
    cout << "--------------------------------\n";
    for (const auto &lex : lexemas)
    {
        cout << lex.token << "\t\t" << lex.lexema << endl;
    }
    return 0;
}