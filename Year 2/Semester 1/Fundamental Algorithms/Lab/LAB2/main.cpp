#include <iostream>
#include <unordered_map>
#include <vector>
#include <fstream>
#include <queue>

int citireLista(std::unordered_map<int, std::vector<int> > &lst, int &n, bool orientat, const std::string &file) {
    std::cout << "CITIRE LISTA ";
    std::cout << ((orientat) ? ("(ORIENTAT)\n") : ("(NEORIENTAT)\n"));
    std::ifstream f(file);

    int x, y;
    f >> n >> x;

    int node;
    f >> node;

    while (f >> x >> y) {
        // n = std::max(n, x);
        if (!lst.contains(x))
            lst[x] = {y};
        else
            lst[x].push_back(y);
        if (!orientat) {
            if (!lst.contains(y))
                lst[y] = {x};
            else
                lst[y].push_back(x);
        }
    }
    f.close();
    return node;
}

void afisareLista(std::unordered_map<int, std::vector<int> > &lst) {
    std::cout << "AFISARE LISTA\n";
    for (const auto &[fst, snd]: lst) {
        std::cout << fst << ": ";
        for (const auto &node: snd)
            std::cout << node << " ";
        std::cout << "\n";
    }
    std::cout << "\n";
}

// ---------------------------

void bfs(std::unordered_map<int, std::vector<int> > &lst) {
    std::queue<int> q;
    std::unordered_map<int, bool> visited;
    const auto aux = lst.begin()->first;

    q.push(aux);
    visited[aux] = true;

    while (!q.empty()) {
        int x = q.front();
        std::cout << x << " ";
        q.pop();

        for (const auto &i: lst[x])
            if (!visited[i]) {
                q.push(i);
                visited[i] = true;
            }
    }
}

void drumMinim(std::unordered_map<int, std::vector<int> > &lst, const int x, std::unordered_map<int, int> &distance) {
    std::queue<int> q;
    std::unordered_map<int, bool> visited;

    distance[x] = 0;
    visited[x] = true;

    q.push(x);
    while (!q.empty()) {
        const int aux = q.front();
        q.pop();

        for (const auto &i: lst[aux])
            if (!visited[i]) {
                q.push(i);
                visited[i] = true;
                distance[i] = distance[aux] + 1;
            }
    }

    for (const auto& i: lst)
        if (!visited[i.first])
            distance[i.first] = -1;
}

// --------------------


void dfs(std::unordered_map<int, std::vector<int>>& lst, std::unordered_map<int, bool>& visited, const int& currentNode) {
    visited[currentNode] = true;
    // std::cout<<currentNode<<" ";

    for (int &i : lst[currentNode])
        if (!visited[i]) {
            visited[i] = true;
            dfs(lst, visited, i);
        }
}

int main() {
    std::unordered_map<int, std::vector<int> > lst;
    int n = 0;
    std::unordered_map<int, int> distance;

    const int x = citireLista(lst, n, true, "grader_test1.in");
    afisareLista(lst);
    std::cout << x << ": ";
    drumMinim(lst, x, distance);
    for (const auto &[fst, snd]: distance)
        std::cout << "(" << fst << ", " << snd << ") ";
    return 0;
}
