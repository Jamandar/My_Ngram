
#include <stdio.h>
#include <stdlib.h>
#define MAX_ARRAY_SIZE 128
void fill_array( int* param_1, char* param_2) {
    int i = 0;
    while( param_2[i ] != '\0') {
        if( param_2[i ] != '"' ) {
            param_1[(int)param_2[i ]]++;
        }
        i ++;
    }
}
void print_array( int* param_1, int string_array ) {
    int i  = 0;
    while(i  < string_array ) {
        if( param_1[i ] > 0 ) {
            printf( "%c:%i\n", i , param_1[i ] );
        }
        i ++;
    }
}
int main ( int ac, char** av ) {
    int x = 1,array[MAX_ARRAY_SIZE] = {0};
    while( x < ac ) {
        fill_array( &array[0], av[x] );
        x++;
    }
    print_array( &array[0], MAX_ARRAY_SIZE );   
    return EXIT_SUCCESS;
}
