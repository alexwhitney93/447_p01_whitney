#include <vector>
#include <algorithm>
#include <string>
#include <ostream>
#include <cstdint> // Use stdint.h if using C.

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

