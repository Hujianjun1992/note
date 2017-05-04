#include <stdio.h>
#include <bitset>
#include <iostream>
using namespace std;

typedef union _data {
    float f;
    char s[4];
} myFloat;


typedef union B_F{
unsigned char b[4];
float f;
}b_f;

int main(void)
{
    float f = 4.5;
    unsigned char * ch = (unsigned char *)(&f);
    for (int i = 0; i < 4; ++i) {
        printf("%x\n", ch[i]);
    }

    unsigned char s[] = {0x00, 0x00, 0x90, 0x40};
    //float * ff = (float *)(s);
    float *ff = reinterpret_cast<float *>(s);
    std::cout << *ff << std::endl;
    return 0;
}
