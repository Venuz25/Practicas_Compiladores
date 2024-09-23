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

vector<Lexema> lexis;

// Función que identifica operadores relacionales
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
                return {lexema, "oprel", "EQ"};  // '=' simple
            else if (carac == '>')
                estado = 6;
            else
                estado = -1;
            break;

        case 1:
            if (carac == '=')
                return {lexema, "oprel", "LE"};  // '<='
            else if (carac == '>')
                return {lexema, "oprel", "NE"};  // '<>'
            else
                return {lexema, "oprel", "LT"};  // '<' simple
            break;

        case 6:
            if (carac == '=')
                return {lexema, "oprel", "GE"};  // '>='
            else
                return {lexema, "oprel", "GT"};  // '>' simple
            break;

        default:
            break;
        }
    }
    return {"desconocido", "desconocido", lexema};
}

// Funciones para identificar palabras clave
Lexema ifi(const string &lexema)
{
    if (lexema == "if")
        return {lexema, "if", ""};
    return {"desconocido", "desconocido", lexema};
}

Lexema elsei(const string &lexema)
{
    if (lexema == "else")
        return {lexema, "else", ""};
    return {"desconocido", "desconocido", lexema};
}

Lexema theni(const string &lexema)
{
    if (lexema == "then")
        return {lexema, "then", ""};
    return {"desconocido", "desconocido", lexema};
}

// Función que identifica identificadores
Lexema Id(const string &lexema)
{
    if (regex_match(lexema, regex("^[a-zA-Z_][a-zA-Z0-9_]*$")))
        return {"id", "id", lexema};
    return {"desconocido", "desconocido", lexema};
}

// Función que identifica números
Lexema Num(const string &lexema)
{
    if (regex_match(lexema, regex("^[0-9]+(\\.[0-9]+)?([eE][+-]?[0-9]+)?$")))
        return {"numero", "numero", lexema};
    return {"desconocido", "desconocido", lexema};
}

// Función para separar tokens
void separaToken(const string &lex)
{
    size_t pos = 0;

    while (pos < lex.length())
    {
        // Espacios
        while (pos < lex.length() && isspace(lex[pos]))
        {
            ++pos;
        }
        if (pos >= lex.length()) break;  // Fin de línea

        // Palabras clave o identificadores
        if (isalpha(lex[pos]) || lex[pos] == '_')
        {
            string tok;
            while ((isalnum(lex[pos]) || lex[pos] == '_') && pos < lex.length())
            {
                tok += lex[pos++];
            }

            // Primero verifica si es una palabra clave
            if (ifi(tok).token != "desconocido")
                lexis.push_back(ifi(tok));
            else if (elsei(tok).token != "desconocido")
                lexis.push_back(elsei(tok));
            else if (theni(tok).token != "desconocido")
                lexis.push_back(theni(tok));
            else
                lexis.push_back(Id(tok));  // Si no es palabra clave, es identificador
        }
        // Números
        else if (isdigit(lex[pos]))
        {
            string tok;
            while ((isdigit(lex[pos]) || lex[pos] == '.' || lex[pos] == 'E' || lex[pos] == 'e' || lex[pos] == '+' || lex[pos] == '-') && pos < lex.length())
            {
                tok += lex[pos++];
            }
            lexis.push_back(Num(tok));
        }
        // Operadores relacionales
        else if (lex[pos] == '>' || lex[pos] == '<' || lex[pos] == '=')
        {
            string tok;
            while ((lex[pos] == '>' || lex[pos] == '<' || lex[pos] == '=') && pos < lex.length())
            {
                tok += lex[pos++];
            }
            lexis.push_back(Opera(tok));
        }
        else
        {
            ++pos;
        }
    }
}

int main()
{
    ifstream archivo("text.txt");
    if (!archivo)
    {
        cerr << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    string linea;
    while (getline(archivo, linea))
    {
        separaToken(linea);
    }
    archivo.close();

    cout << "  TOKEN\t\t  |\t\tLEXEMA\t\t  |\tVALOR DE ATRIBUTO\n";
    cout << "-------------------------------------------------------\n";
    for (const auto &lex : lexis)
    {
        cout << "  " << lex.token << "\t\t  |\t\t\t" << lex.lexema << "\t\t  |\t\t\t" << lex.valAtri << endl;
    }
    return 0;
}
