struct elements {
	 	int len; 
		void* inner;
};
struct factory {
	 	struct elements factory_inner;
};

int main() {
    struct factory_inner_1 = {
		.len = 256,    
		.inner = malloc(256) 
    };

    struct factory_inner_2 = {
        .len = 8,    
        .inner = malloc(8) 
    };

    struct factory thread_thread = {
        .factory_inner = factory_inner_1,
    };
    struct factory proxy_thread = {
        .factory_inner = factory_inner_2,
    };
}
