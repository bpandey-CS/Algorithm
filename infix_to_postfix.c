// infix to postfix expression conversion
// stack and  queue implementation in c;
#include <stdio.h>
#include<stdlib.h>
#define MAX 100
#define DEFUALTSIZE 10

char pop(char *stack, int *top);
void push(char* stack, int *top, char item);
char *resize(char *p, int capacity);
int preceedence(char op); // takes in chracter and gives operator preceedence 
enum oper{minus, plus, divide, multiply, bitwiseand, dollar, rightbracket, leftbracket}; 

void main(){
    int count=0, capacity=DEFUALTSIZE, pre;
    char *output, *stack, o;
    output = (char *)malloc(DEFUALTSIZE);
    stack = (char *)malloc(DEFUALTSIZE);
    int top = -1;
    char ch;
    printf("Input an Expression \n");
    while((ch = getchar()) != '\n'){
        if(count == capacity){
            output = resize(output, capacity);
            stack = resize(stack, capacity);
            if(stack == NULL || output == NULL){
                printf("\n Heap Memory overflow");
                exit(EXIT_FAILURE);
            }
            capacity = capacity + DEFUALTSIZE;
        }
        pre = preceedence(ch);
        if(pre == -999){
            // found an operand
            output[count++] = ch;
        }
        else if(ch == ')'){
            while((o = pop(stack, &top)) != '('){
                if(o == '\0'){
                    exit(EXIT_FAILURE);
                }
                output[count++] = o;
            }
        }
        else{
            // ch is an operator or a '('
            if (ch == '(' || top == -1){
                push(stack, &top, ch);
            }
            else{
                while(preceedence(stack[top]) >= pre && stack[top] != '('){
                    o = pop(stack, &top);
                    if(o == '\0'){
                        exit(EXIT_FAILURE);
                    }
                    output[count++] = o;
                }
                push(stack, &top, ch);
            }
        }
    }
    // pop off left overs from stack 
    
    while(top > -1){
        if ((o=pop(stack, &top)) != '(')
            output[count++] = o;
    }
    puts(output);
    free(output);
    free(stack);
    return;
}

void push(char* stack, int *top, char item){
    stack[++*top] = item;
    return;
}

char pop(char *stack, int *top){
    if (*top == -1){
        printf("\n Stack underflow");
        return '\0';
    }
    else{
        char item = stack[(*top)--];
        return item;
    }
}

char *resize(char *p, int capacity){
    return realloc(p, capacity+DEFUALTSIZE);
}

int preceedence(char op){
    enum oper prec;
    switch(op){
        case '+':;
                prec = plus;
                return prec;
        case '-':;
                prec = minus;
                return prec;
        case '/':;
                prec = divide;
                return prec;
        case '*':;
                prec = multiply;
                return prec;
        case '$':;
                prec = dollar;
                return prec;
        case ')':;
                prec = rightbracket;
                return prec;
        case '(':;
                prec = leftbracket;
                return prec;
        case '^':;
                prec = bitwiseand;
                return prec;
        default : return -999;
    }
}
