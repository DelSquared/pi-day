#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//Date created 14-3-2014

int main()
{
    unsigned int i, c, in=0;
    double x,y,z, pi, i1, in1;
    //input number of simulations, as a rule of thumb, take a rate of ~1500sims/sec//
    printf("Input number of simulations:\n")
    scanf("%lld", &i);
    i1=i;

    for (c=1;c!=i;c++)
    {
        y = (double)rand()/RAND_MAX;
        x = (double)rand()/RAND_MAX;
        printf("x=%lf y=%lf\n", x, y);
        z=x*x+y*y;
        printf("z=%lf\n", z);
        if (z<1) {in=in+1;}
        printf("i=%d in=%d\n", i, in);
        in1=in;
    }

    pi=(in1/i1)*4;
    printf("%lf",pi);

}
