# Table3 AE

## Instructions to reproduce

We manually collect all the bugs reported in the RFL community. 
The data is stored in the `data/bug_list.md` file.
You can check the bug list in that file.

### Table3

![alt text](image.png)

### Table 3 format illustration and its relation with `bug_list`

1. Table 3 illustration
The bugs reports are from three sources: `Github`, `Mailling list`, and `Intel LKP`, which consists of three rows of Table 3.
We classify bugs as `security` bugs and `unsound` bugs which corresponds to the two columns of Table 3 seperatelly.
The numbers in the brackets are the number of merged and staged bugs.

2. Relation with `bug_list`
The rows mentioned above are listed in different sections and `security` and `unsound` bug blocks are listed in each section.
In each block, we present bug numbers at first, then list bug links in the `items` part.
The specific numbers of different states, such as open/close state, merged/staged/reviewing state and type state are attached later.