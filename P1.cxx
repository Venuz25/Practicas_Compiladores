#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <regex>
using namespace std;

struct Lexema {
    string token;
    string lexema;
};

// determinar el token
string obtenerToken(const string &lexema) {
     // Tipos de variables
    if (lexema == "int" || lexema == "float" || lexema == "double" || lexema == "char" || lexema == "string" || lexema == "bool") 
        return "tipo_variable";

    // Condicionales
    if (lexema == "&&" || lexema == "||") 
        return "condicional";

    // Operadores de comparación
    if (lexema == "<" || lexema == ">" || lexema == "<=" || lexema == ">=" || lexema == "==" || lexema == "!=") 
        return "comparacion";

    // if, else
    if (lexema == "if") 
        return "if";
    if (lexema == "else") 
        return "else";

    // números
    if (regex_match(lexema, regex("^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$"))) 
        return "numero";

    // Identificadores
    if (isalpha(lexema[0]) || lexema[0] == '_') 
        return "id";

    // Literales
    if (lexema[0] == '"' && lexema[lexema.size() - 1] == '"') 
        return "literal";

    return "desconocido";
}

int main() {
    ifstream archivo("Texto.txt");
    if (!archivo) {
        cerr << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    vector<Lexema> lexemas;
    string palabra;

    while (archivo >> palabra) {
        Lexema lex;
        lex.lexema = palabra;
        lex.token = obtenerToken(palabra);
        lexemas.push_back(lex);
    }

    // Imprimir lexemas y tokens
    cout << "TOKEN          LEXEMA\n";
    cout << "----------------------\n";
    for (const auto &lex : lexemas) {
        cout << lex.token << "          " << lex.lexema << endl;
    }

    return 0;
}
