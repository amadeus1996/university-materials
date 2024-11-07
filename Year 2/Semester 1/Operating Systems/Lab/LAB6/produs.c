#include <stdio.h>
#include <pthread.h> // threads
#include <errno.h>   // errno
#include <stdlib.h>  // malloc

struct args {
  int **matrix1, **matrix2;
  int numOfElements;
  int multipliedRow, multipliedColumn;
};

void print(int** matrix, int m, int n) {
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j)
      printf("%d ", matrix[i][j]);
    printf("\n");
  }
  printf("\n");
}

void* multiply(void *v) {
  struct args* arguments = v;
  int *result = malloc(sizeof(int));
  *result = 0;
  
  for (int i = 0; i < arguments->numOfElements; ++i)
    *result += arguments->matrix1[arguments->multipliedRow][i] * arguments->matrix2[i][arguments->multipliedColumn];
    
  return result;
}

int main(int argc, char** argv) {
  if (argc != 5 || atoi(argv[2]) != atoi(argv[3])) {
    printf("Invalid input\n");
    return 0;
  }

  int m1 = atoi(argv[1]); // nr. linii (1)
  int n1_m2 = atoi(argv[2]); // nr coloane (1) SI nr. linii (2)
  int n2 = atoi(argv[4]); // nr coloane (2)
  
  int **matrix1 = malloc(m1 * sizeof(int*));
  for (int i = 0; i < m1; ++i)
    matrix1[i] = malloc(n1_m2 * sizeof(int));   
  int **matrix2 = malloc(n1_m2 * sizeof(int*));
  for (int i = 0; i < n1_m2; ++i)
    matrix2[i] = malloc(n2 * sizeof(int)); 
  int **matrix3 = malloc(m1 * sizeof(int*));
  for (int i = 0; i < m1; ++i)
    matrix3[i] = malloc(n2 * sizeof(int));
  
  for (int i = 0; i < m1; ++i)
    for (int j = 0; j < n1_m2; ++j)
      matrix1[i][j] = i * n1_m2 + j + 1;
  print(matrix1, m1, n1_m2);
  for (int i = 0; i < n1_m2; ++i)
    for (int j = 0; j < n2; ++j)
      matrix2[i][j] = i * n2 + j + 1;
    print(matrix2, n1_m2, n2);
    
  struct args arguments = {matrix1, matrix2, n1_m2, 0, 0};
  for (int i = 0; i < m1; ++i)
    for (int j = 0; j < n2; ++j) {
      arguments.multipliedRow = i;
      arguments.multipliedColumn = j;
      
      pthread_t thr;
      if (pthread_create(&thr, NULL, multiply, &arguments)) { // vezi de ce tre sa pui & (altfel da eroare dar nush dc)
        perror(NULL);
        return errno;
      }
      
      void* result;
      if (pthread_join(thr, &result)) {
        perror(NULL);
        return errno;
      }
      
      matrix3[i][j] = *(int*)result;
      free(result);
    }
  print(matrix3, m1, n2);
  
  for (int i = 0; i < m1; ++i)
    free(matrix3[i]);
  free(matrix3);
  for (int i = 0; i < n1_m2; ++i)
    free(matrix2[i]);
  free(matrix2);
  for (int i = 0; i < m1; ++i)
    free(matrix1[i]);
  free(matrix1);
  return 0;
}
