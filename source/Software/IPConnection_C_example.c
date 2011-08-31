// tested with 
// gcc -lpthread -lrt -o example ip_connection.c example.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"

#define HOST "localhost"
#define PORT 4223

void cb_enumerate(char *uid, char *name, uint8_t stack_id, bool is_new) {
	if(is_new) {
		printf("New device:\n");
	} else {
		printf("Removed device:\n");
	}

	printf(" Name:     %s\n", name);
	printf(" UID:      %s\n", uid);
	printf(" Stack ID: %d\n", stack_id);
	printf("\n");
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	ipcon_enumerate(&ipcon, cb_enumerate);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}