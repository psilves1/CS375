#include <iostream>

int iterFib(int n);

int main(int argc, char *argv[]){

    long arg = strtol(argv[1], NULL, 10);

    for(int i = 1; i < 1000000; i++){
      iterFib(arg);
    }
        std::cout << iterFib(arg) << std::endl;
}


/** n is the nth number in fib seq**/ 
int iterFib(int n){

    int a = 0;
    int b = 1;
    int temp = 0;

    for(int i = 0; i < n; i++){

        temp = b;
        b += a;
        a = temp; 
    }

    return a+b;
}
