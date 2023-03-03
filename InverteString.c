/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <string.h>

int main()
{
    char nome[81];
    int i =6, aux =0;
    printf("\nDigite uma palavra de 8 letras: ");
    fgets(nome,10,stdin);
    nome[strlen(nome)-1]='\0';
    
    for(i=8;i>=0;i--){
        printf("%c",nome[i]);
    }
    
}
