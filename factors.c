#include <stdio.h>

int main()
{
    long long int number = 239809320265259;
    long int factor1 = 2;
    long int factor2;

    while (number % factor1)
    {
        if (factor1 <= number)
        {
            factor1++;
        }
        else {
            return (-1);
        }
    }

    factor2 = number / factor1;
    printf("%lld = %ld * %ld\n", number, factor2, factor1);
    return (0);
}
