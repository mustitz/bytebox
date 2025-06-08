#include <bytebox/chronicle.h>

int main()
{
    struct bbchronicle * tmp = new_chronicle(BBCHRONICLE_ALL);
    del_chronicle(tmp);
    return 0;
}
