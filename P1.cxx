#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <regex>

using namespace std;
bool lit = false, com = false;

struct Lexema
{
    string token;
    string lexema;
};

// determinar el token
string obtenerToken(const string &lexema)
{
    // Literales
    if (lexema[0] == '"'){
        lit = true;
        return "literal";
    }else if(lexema[lexema.size()-1] == '"'){
        lit = false;
        return "literal";
    }
    else if(lit)
        return "literal";

    //comentario
    if (lexema.substr(0, 2) == "/*"){
        com = true;
        return "comentario";
    }else if(lexema.substr(0, 2) == "*/" || (lexema.length() > 2 && lexema.substr(lexema.size()-2, 2) == "*/")){
        com = false;
        return "comentario";
    }
    else if(com)
        return "comentario";
    
    // Tipos de variables
    if (lexema == "int" || lexema == "float" || lexema == "double" || lexema == "char" || lexema == "string" || lexema == "bool")
        return "tipo_variable";

    // Condicionales
    if (lexema == "&&" || lexema == "||")
        return "condicional";

    // Operadores de comparación
    if (lexema == "<" || lexema == ">" || lexema == "<=" || lexema == ">=" || lexema == "==" || lexema == "!=")
        return "comparacion";

    //operadores aritmeticos
    if(lexema == "+" || lexema == "-" || lexema == "*" || lexema == "/" || lexema == "^")
        return "aritmetico";

    //operadores ternarios
    if(lexema == "?" || lexema == ":")
        return "ternario";

    // if, else
    if (lexema == "if")
        return "if";

    if (lexema == "else")
        return "else";
    
    //return
    if(lexema == "return")
        return "return";

    // números
    if (regex_match(lexema, regex("^-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?$")))
        return "numero";

    // Identificadores
    if (isalpha(lexema[0]) || lexema[0] == '_')
        return "id";

    return "desconocido";
}

int main()
{
    ifstream archivo("Texto.txt");
    if (!archivo)
    {
        cerr << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    vector<Lexema> lexemas;
    string palabra, linea;

    while (getline(archivo, linea))
    {
        stringstream palabras(linea);
        while (palabras >> palabra)
        {
            Lexema lex;

            if(palabra != "(" && palabra != ")" && palabra != "{" && palabra != "}" && palabra != "[" && palabra != "]"){
                for(char c : palabra){
                    if(c != '"'){
                        lex.lexema += c;
                    }
                } 

                lex.token = obtenerToken(palabra);

                if(palabra.substr(0, 2) != "/*" && (palabra.substr(0, 2) != "*/" || (palabra.length() > 2 && palabra.substr(palabra.size()-2, 2) != "*/"))){
                    lexemas.push_back(lex);
                }
            }
        }
    }

    // Imprimir lexemas y tokens
    cout << "TOKEN               LEXEMA\n";
    cout << "--------------------------------\n";
    for (const auto &lex : lexemas)
    {
        cout << lex.token << "\t\t" << lex.lexema << endl;
    }

    return 0;
}
