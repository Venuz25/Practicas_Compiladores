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

Lexema Opera(const string &lexema)
{
    int estado = 0;
    char carac;

    for (size_t i = 0; i < lexema.length(); i++)
    {
        carac = lexema[i];

        switch (estado)
        {
        case 0:
            if (carac == '<')
                estado = 1;
            else if (carac == '=')
                estado = 5;
            else if (carac == '>')
                estado = 6;
            else
                estado = -1;
            break;

        case 1:
            if (carac == '=')
                return {lexema, "oprel", "LE"};
            else if (carac == '>')
                return {lexema, "oprel", "NE"};
            else
                return {lexema, "oprel", "LT"};
            break;

        case 5:
            return {lexema, "oprel", "EQ"};
            break;

        case 6:
            if (carac == '=')
                return {lexema, "oprel", "GE"};
            else
                return {lexema, "oprel", "GT"};
            break;

        default:
            break;
        }
    }
}

Lexema ifi(const string &lexema)
{
    int estado = 0;
    char carac;

    for (size_t i = 0; i < lexema.length(); i++)
    {
        carac = lexema[i];
        switch (estado)
        {
        case 0:
            if (carac == 'i')
                estado = 1;
            else
                estado - 1;
            break;
        case 1:
            if (carac == 'f')
                estado = 2;
            else
                estado = -1;
            break;
        case 2:
            return {lexema, "if", ""};
            break;
        default:
            break;
        }
    }
}
Lexema elsei(const string &lexema)
{
    int estado = 0;
    char carac;
    for (size_t i = 0; i < lexema.length(); i++)
    {
        carac = lexema[i];
        switch (estado)
        {
        case 0:
            if (carac == 'e')
                estado = 1;
            else
                estado = -1;
            break;
        case 1:
            if (carac == 'l')
                estado = 2;
            else
                estado = -1;
            break;
        case 2:
            if (carac == 's')
                estado = 3;
            else
                estado = -1;
            break;
        case 3:
            if (carac == 'e')
                estado = 4;
            else
                estado = -1;
            break;
        case 4:
            return {lexema, "else", ""};
            break;
        default:
            break;
        }
    }
}
Lexema theni(const string &lexema)
{
    int estado = 0;
    char carac;

    for (size_t i = 0; i < lexema.length(); i++)
    {
        carac = lexema[i];
        switch (estado)
        {
        case 0:
            if (carac == 't')
                estado = 1;
            else
                estado = -1;
            break;
        case 1:
            if (carac == 'h')
                estado = 2;
            else
                estado = -1;
            break;
        case 2:
            if (carac == 'e')
                estado = 3;
            else
                estado = -1;
            break;
        case 3:
            if (carac == 'n')
                estado = 4;
            else
                estado = -1;
            break;
        case 4:
            return {lexema, "then", ""};
            break;
        default:
            break;
        }
    }
}

Lexema Id(const string &lexema)
{
    int estado = 0;
    char carac;

    for (size_t i = 0; i < lexema.length(); i++)
    {
        carac = lexema[i];

        switch (estado)
        {
        case 0:
            if(isalpha(carac) || carac == '_') estado = 1;
            else estado = -1;
            break;
        
        case 1:
            if(isalnum(carac) || carac == '_') estado = 1;
            else estado = -1;
            break;

        default:
            break;
        }
    }

    if(estado == 1){
        return {"id", "id", lexema};
    }
}

Lexema Num(const string &lexema)
{
    int estado = 0;
    char carac;
    for (size_t i = 0; i < lexema.length(); i++)
    {
        carac = lexema[i];

        switch (estado)
        {
        case 0:
            if(isdigit(carac)) estado = 1;
            else estado = -1;
            break;
        
        case 1: //digito
            if(isdigit(carac)) estado = 1;
            else if(carac == '.') estado = 2;
            else if(carac == 'E'||carac == 'e') estado = 4;
            else estado = -1;
            break;
        
        case 2:
            if(isdigit(carac)) estado = 3;
            else -1;
            break;
        
        case 3: //digito
            if(isdigit(carac)) estado = 3;
            else if(carac == 'E'||carac == 'e') estado = 4;
            else estado = -1;
            break;
        
        case 4:
            if(carac == '+' || carac == '-') estado = 5;
            else if(isdigit(carac)) estado = 6;
            else estado = -1;
            break;
        
        case 5:
            if(isdigit(carac)) estado = 6;
            else estado =-1;
            break;

        case 6: //digito
            if(isdigit(carac)) estado = 6;
            else estado = -1;
            break;
        default:
            break;
        }
    }
    if(estado == 1 || estado == 3 || estado == 6 ){
        return {"numero", "numero", lexema};
    }
}

int main()
{
    ifstream archivo("Text.txt");
    if (!archivo)
    {
        cerr << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    vector<Lexema> lexemas;
    string palabra, linea;
    size_t position;
    while (getline(archivo, linea))
    {
        stringstream palabras(linea);
        while (palabras >> palabra)
        {
        }
    }

    cout << "TOKEN\t\t\t|\t\t\tLEXEMA\t\t\t|\t\t\tVALOR DE ATRIBUTO\n";
    cout << "--------------------------------\n";
    for (const auto &lex : lexemas)
    {
        cout << lex.token << "\t\t" << lex.lexema << endl;
    }
    return 0;
}