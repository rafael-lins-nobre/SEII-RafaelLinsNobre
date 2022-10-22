#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
    pid_t child_pid;

    printf("O ID do processo do programa principal é %d\n", (int) getpid());

    child_pid = fork();
    if(child_pid != 0){
        printf("Este é o processo pai, com ID %d\n", (int)getpid());
        printf("O ID do processo filho é %d\n", (int)child_pid);

    }
    else{
        printf("Este é o processo filho, com ID %d\n", (int)getpid());
    }
    return 0;
}