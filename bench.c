#include <stdio.h>

int main(void) {
    __int128 sum = 0;

    for (long long i = 1; i <= 100000; i++)
        sum += (__int128)i * i;

    // Print __int128 manually
    char buffer[50];
    int pos = 0;

    if (sum == 0) {
        putchar('0');
        return 0;
    }

    while (sum > 0) {
        buffer[pos++] = '0' + (sum % 10);
        sum /= 10;
    }

    while (pos--)
        putchar(buffer[pos]);

    putchar('\n');

    return 0;
}
