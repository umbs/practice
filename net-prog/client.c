#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>

void client() {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serv_addr;

    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(5000);
    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);

    connect(fd, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

    return;
}

void main() {
    client();
}
