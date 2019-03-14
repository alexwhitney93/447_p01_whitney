#include <vector>
#include <algorithm>
#include <string>
#include <ostream>
#include <cstdint> // Use stdint.h if using C.
#include <fstream>
#include <iostream>

struct TrainingHeader
{
    char type_string[8];
    uint64_t id;
    uint64_t n_points;
    uint64_t n_dims;
} __attribute__((packed));

struct QueryHeader
{
	char type_string[8];
    uint64_t id;
    uint64_t n_queries;
    uint64_t n_dims;
	uint64_t n_neighbors;
} __attribute__((packed));

struct ResultsHeader
{
    char type_string[8];
    uint64_t t_id;
	uint64_t q_id;
	uint64_t r_id;
    uint64_t n_queries;
    uint64_t n_dims;
	uint64_t n_neighbors;
} __attribute__((packed));

int
main(int argc, char **argv)
{
	/*if(argc != 5)
	{
		std::cerr << "usage: ./k-nn n-cores training_file query_file result_file" << std::endl;
	}*/
	int n_cores = atoi(argv[1]);
	TrainingHeader t_header;
	QueryHeader q_header;
	ResultsHeader r_header;
	std::ifstream training_file; 
    training_file.open(argv[2], std::ios::binary | std::ios::in);
    char* c_temp;
    training_file.read(c_temp, 8); // read 8 bytes
    long l_temp = atol(c_temp);
	t_header.id = (unsigned int) l_temp;
    training_file.read(c_temp, 8); // read 8 bytes
    l_temp = atol(c_temp);
	t_header.n_points = (unsigned int) l_temp;
    training_file.read(c_temp, 8); // read 8 bytes
    l_temp = atol(c_temp);
	t_header.n_dims = (unsigned int) l_temp;
	/*
    training_file.read(t_header.id, 8);
    training_file.read(t_header.n_points, 8);
    training_file.read(t_header.n_dims, 8);
    */
}
