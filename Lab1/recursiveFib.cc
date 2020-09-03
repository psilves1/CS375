#include <iostream>

int recursiveFib(int n, int a, int b);

int main(int argc, char *argv[]){  

    long arg = strtol(argv[1], NULL, 10);

    /*
    for(int i = 1; i < 1000000; i++){
      recursiveFib(arg, 0, 1);
    }
    */
    
   std::cout << recursiveFib(arg, 0, 1) << std::endl;
}



/** n is the nth number in fib seq**/ 
int recursiveFib(int n, int a = 0, int b = 1){

    if(n == 0)
        return 0;

    if (n == 1) 
        return 1;

    return recursiveFib(n-1)+recursiveFib(n-2);
    
}

