# easy of programming

## environment

### ycombinator

be7cdac3875e:/data/bupt-rtos/rust-e1000/ycombinator

### lwn

### reddit

## collect data && analyze

### lwn

```bash
## method 1
python .\crawl.py
# delete the last line of `p_titles.txt`
python .\title_lines.py
# concact the line of "beyond 4096 bytes" with the above one of `new_pt_titles.txt`
python delete_duplicate.py
# get the titles
# get the real titles
# find the urls
# crawl all the commands
# use chatgpt to filter them
## method 2
```

```bash
grep "\\nPositive" -nR lwn* | wc -l #148 # 40
grep "\\nNegative" -nR lwn* | wc -l #216 # 63
```

### reddit

### ycombinator

```bash
goto the website of https://hn.algolia.com/?q=rust

# wget the links

python3 clean_data.py
python3 openai_new.py

grep "\\nPositive" -nR stat_* | wc -l #148
grep "\\nNegative" -nR stat_* | wc -l #216

# plot the pics
python plt.py
```



Safety and Memory Safety (Total: 43 Mentions):

Rust's safety features, memory safety, and elimination of vulnerabilities in C code. (43 Mentions)
Compatibility and Integration (Total: 11 Mentions):

Rust's compatibility with the Linux kernel, APIs, and architectures. (11 Mentions)
Performance and Efficiency (Total: 7 Mentions):

Rust's potential to improve performance, efficiency, and optimization. (7 Mentions)
Code Quality and Standards (Total: 6 Mentions):

Rust's impact on code quality, standards, and reliability. (6 Mentions)
Expressiveness and Features (Total: 4 Mentions):

Rust's expressiveness, features, and advantages in code development. (4 Mentions)

Safety and Memory Safety 
Compatibility and Integration 
Performance and Efficiency 
Code Quality and Standards 
Expressiveness and Features 


Learning Curve and Complexity 
Kernel Compatibility 
Resource Allocation 
Developer Sentiment 
Advocacy and Hype 

Learning Curve and Complexity (Total: 30 Mentions):

Concerns about the learning curve, complexity, and challenges in understanding Rust. (30 Mentions)
Kernel Compatibility (Total: 16 Mentions):

Concerns regarding Rust's compatibility with the Linux kernel, existing APIs, and architectures. (16 Mentions)
Resource Allocation (Total: 12 Mentions):

Concerns about resource allocation, including the potential diversion of resources and expertise. (12 Mentions)
Developer Sentiment (Total: 29 Mentions):

Concerns related to how developers perceive Rust, including resistance to change and cultural differences. (29 Mentions)
Advocacy and Hype (Total: 11 Mentions):

Concerns regarding overzealous Rust advocacy, excessive hype, and misalignment with kernel culture. (11 Mentions)