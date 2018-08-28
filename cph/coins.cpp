#include <cmath>        // INFINITY
#include <algorithm>    // min
#include <iostream>     // cout
#include <chrono>       // timers

using namespace std;
using namespace std::chrono;

int coins[] = {1, 5, 10, 25, 50};
int call_count = 0;

int solve(int x) {
    call_count++;
    if (x < 0) return INFINITY;
    if (x == 0) return 0;
    int best = INFINITY;
    for (auto c : coins) {
       best = min(best, solve(x-c)+1);
    }
    return best;
}

int main() {

    for (int i=21; i<61; i++) {
        auto start = high_resolution_clock::now();
        call_count = 0;
        int result = solve(i);
        auto end = high_resolution_clock::now();

        //auto duration = duration_cast<microseconds>(end - start);
        auto duration = duration_cast<milliseconds>(end - start);

        cout << "Input: " << i << "; Result: " << result << "; " ;
        cout << "Compute time: " << duration.count() << " msec; ";
        cout << "Call count: " << call_count << endl;
    }

    return EXIT_SUCCESS;
}
