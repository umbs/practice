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

void server() {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serv_addr;

    memset(&serv_addr, 0, sizeof(serv_addr));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(5000);

    bind(fd, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
    listen(fd, 10); // 10 connections??

    while(1) {
        int client_fd = accept(fd, (struct sockaddr *)NULL, NULL);

        printf("Received a connection from client: %d\n", client_fd);

        close(client_fd);
    }
}

void main() {
    server();
}
