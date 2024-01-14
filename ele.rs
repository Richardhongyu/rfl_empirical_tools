pub struct elements<const N: usize> {
    inner: [i32; N],
}

trait dyn_num {
    fn use_elements(&self);
}

pub struct factory {
    foo: i32,
    factory_inner: &'static dyn dyn_num
}

struct thread<const T: usize>{
    thread_elements: elements<T>,
}

impl dyn_num for thread<256> {
    fn use_elements(&self) -> i32 {
        256
    }
}

struct proxy<const T: usize>{
    proxy_elements: elements<T>,
}

impl dyn_num for proxy<8> {
    fn use_elements(&self) -> i32 {
        8
    }
}

static thread_factory_inner: thread<256> = thread {
    thread_elements: elements { inner: [0; 256] },
};

static proxy_factory_inner: proxy<8> = proxy {
    proxy_elements: elements { inner: [1; 8] },
};

fn main() {
    let thread_factory = factory { 
        foo: 0, 
        factory_inner: &thread_factory_inner 
    };

    let proxy_factory = factory { 
        foo: 1, 
        factory_inner: &proxy_factory_inner 
    };
}