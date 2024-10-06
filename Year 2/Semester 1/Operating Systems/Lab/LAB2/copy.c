#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    char src[20];
    char dest[20];

    // READ THE NAME OF THE SOURCE FILE
    ssize_t src_bytes   = syscall(0, 0, src, sizeof(src));
    (src[src_bytes - 1] = '\n') ? (src[src_bytes - 1] = '\0') : (src[src_bytes] = '\0');

    // OPEN THE SOURCE FILE
    int open_src = syscall(2, src, O_RDONLY);
    if (open_src == -1) {
        perror("Error");
        return -1;
    }

    // PRINT THE SOURCE FILE
    // syscall(1, STDOUT_FILENO, src, src_bytes);
    // syscall(1, STDOUT_FILENO, "\n", 1);

    // READ THE NAME OF THE DESTINATION FILE
    ssize_t dest_bytes    = syscall(0, 0, dest, sizeof(dest));
    (dest[dest_bytes - 1] = '\n') ? (dest[dest_bytes - 1] = '\0') : (dest[dest_bytes] = '\0');

    // OPEN THE DESTINATION FILE
    int open_dest = syscall(2, dest, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (open_dest == -1) {
        perror("Error");
        return -1;
    }

    // PRINT THE DESTINATION FILE
    // syscall(1, STDOUT_FILENO, dest, dest_bytes);
    // syscall(1, STDOUT_FILENO, "\n", 1);

    // GET THE LENGTH OF THE TEXT IN THE SOURCE FILE
    struct stat src_stat;
    syscall(4, src, &src_stat);
    ssize_t src_size = src_stat.st_size;
    
    // COPY THE CONTENTS OF THE SOURCE TO THE DESTINATION
    char src_text[src_size];
    syscall(0, open_src, src_text, src_size);
    syscall(1, open_dest, src_text, src_size);

    // CLOSE BOTH FILES
    syscall(3, open_src);
    syscall(3, open_dest);

    return 0;
}
