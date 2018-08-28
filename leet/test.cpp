using namespace std;

int solve(int x) {
    if (x < 0) return INF;
    if (x == 0) return 0;
    int best = INF;
    for (auto c : coins) {
       best = min(best, solve(x-c)+1);
    }
    return best;
}

int main() {
    // solution comes here

}