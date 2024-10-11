#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

void citireLista(std::unordered_map<int, std::vector<int>>& lst, int& n, bool orientat) {
    std::cout<<"CITIRE LISTA ";
    std::cout<<((orientat) ? ("(ORIENTAT)\n") : ("(NEORIENTAT)\n"));
    std::ifstream f ("lista.in");
    int x, y;
    while (f>>x>>y) {
        n = std::max(n, std::max(x, y));
        if (lst.find(x) == lst.end())
            lst[x] = {y};
        else
            lst[x].push_back(y);
        if (!orientat) {
            if (lst.find(y) == lst.end())
                lst[y] = {x};
            else
                lst[y].push_back(x);
        }
    }
    f.close();
}

void afisareLista(std::unordered_map<int, std::vector<int>>& lst) {
    std::cout<<"AFISARE LISTA\n";
    for (const auto& pair : lst) {
        std::cout<<pair.first<<": ";
        for (const auto& node : pair.second)
            std::cout<<node<<" ";
        std::cout<<"\n";
    }
    std::cout<<"\n";
}

// ----------------------------------------------------------------

void citireMatrice(int**& matr, int &n, bool orientat) {
    std::cout<<"CITIRE MATRICE ";
    std::cout<<((orientat) ? ("(ORIENTAT)\n") : ("(NEORIENTAT)\n"));
    std::ifstream f ("matrice.in");
    f>>n;

    matr = new int*[n];
    for (int i = 0; i < n; ++i) {
        matr[i] = new int[n];
        for (int j = 0; j < n; ++j)
            matr[i][j] = 0;
    }
    
    int x, y;
    while (f>>x>>y) {
        matr[x - 1][y - 1] = 1;
        if (!orientat)
            matr[y - 1][x - 1] = 1;
    }
    f.close();
}

void afisareMatrice(int**& matr, int n) {
    std::cout<<"AFISARE MATRICE\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j)
            std::cout<<matr[i][j]<<" ";
        std::cout<<"\n";
    }
    std::cout<<"\n";
}

// ----------------------------------------------------------------

void listaToMatrice(std::unordered_map<int, std::vector<int>>& lst, int**& matr, int &n, bool orientat) {
    std::cout<<"LISTA -> MATRICE ";
    std::cout<<((orientat) ? ("(ORIENTAT)\n") : ("(NEORIENTAT)\n"));
    matr = new int*[n];
    for (int i = 0; i < n; ++i) {
        matr[i] = new int[n];
        for (int j = 0; j < n; ++j)
            matr[i][j] = 0;
    }

    for (auto it = lst.begin(); it != lst.end();) {
        for (auto& node : it->second) {
            matr[it->first - 1][node - 1] = 1;
            if (!orientat)
                matr[node - 1][it->first - 1] = 1;
        }
        it = lst.erase(it);
    }
}

void matriceToLista(std::unordered_map<int, std::vector<int>>& lst, int**& matr, int &n, bool orientat) {
    std::cout<<"MATRICE -> LISTA ";
    std::cout<<((orientat) ? ("(ORIENTAT)\n") : ("(NEORIENTAT)\n"));

    if (orientat) {
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (matr[i][j]) {
                    if (lst.find(i + 1) == lst.end())
                        lst[i + 1] = {j + 1};
                    else
                        lst[i + 1].push_back(j + 1);
                    matr[i][j] = 0;
                }
    } 

    else {
        for (int i = 0; i < n - 1; ++i)
            for (int j = i + 1; j < n; ++j)
                if (matr[i][j]) {
                    if (lst.find(i + 1) == lst.end())
                        lst[i + 1] = {j + 1};
                    else
                        lst[i + 1].push_back(j + 1);
                    if (lst.find(j + 1) == lst.end())
                        lst[j + 1] = {i + 1};
                    else
                        lst[j + 1].push_back(i + 1);
                    matr[i][j] = 0, matr[j][i] = 0;
                }
    }
}

void interschimbareReprezentare(std::unordered_map<int, std::vector<int>>& lst, int**& matr, int& n, bool reprez, bool orientat) {
    // lst, matr: ARGUMENTELE CARE STOCHEAZA REPREZENTAREA GRAFULUI
    // m, n:      NUMARUL DE LINII/COLOANE PT MATRICEA DE ADIACENTA
    // reprez:    0 = AVEM MATRICEA DE TRANSFORMAT IN LISTA, 1 = AVEM LISTA DE TRANSFORMAT IN MATRICE
    // orientat:  0 = GRAF NEORIENTAT, 1 = GRAF ORIENTAT

    if (reprez) // LISTA DE TRANSFORMAT IN MATRICE
        listaToMatrice(lst, matr, n, orientat); 
    else        // MATRICE DE TRANSFORMAT IN LISTA
        matriceToLista(lst, matr, n, orientat);
}

int main() {
    // CITIRE + AFISARE: LISTA DE ADIACENTA
    std::unordered_map<int, std::vector<int>> lst;
    int n = 0;
    citireLista(lst, n, false); // CITIRE LISTA, GRAF NEORIENTAT
    // citireLista(lst, n, true);     // CITIRE LISTA, GRAF ORIENTAT
    afisareLista(lst); 

    // CITIRE + AFISARE: MATRICE DE ADIACENTA
    int** matr = nullptr;
    citireMatrice(matr, n, false); // CITIRE MATRICE, GRAF NEORIENTAT
    // citireMatrice(matr, n, true);  // CITIRE MATRICE, GRAF ORIENTAT
    afisareMatrice(matr, n);

    // interschimbareReprezentare(lst, matr, n, 1, false);    // LISTA -> MATRICE, GRAF NEORIENTAT
    // interschimbareReprezentare(lst, matr, n, 1, true);     // LISTA -> MATRICE, GRAF ORIENTAT
    // afisareLista(lst);
    // afisareMatrice(matr, n);

    // interschimbareReprezentare(lst, matr, n, 0, false); // MATRICE -> LISTA, GRAF NEORIENTAT
    // interschimbareReprezentare(lst, matr, n, 0, true);  // MATRICE -> LISTA, GRAF ORIENTAT
    // afisareLista(lst);
    // afisareMatrice(matr, n);

    // ELIBERARE MEMORIE PT MATRICE ALOCATA DINAMIC
    for (int i = 0; i < n; ++i)
        delete[] matr[i];
    delete[] matr;
    return 0;
}
