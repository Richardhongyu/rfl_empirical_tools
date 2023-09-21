# classifaction

## environment

previous:root@c6ef5be60e4f:/data/bupt-rtos/rfl/rust-for-linux#
now:root@c6ef5be60e4f:/data/bupt-rtos/test/rust-for-linux#

## get emails

```bash
git clone --mirror http://lore.kernel.org/rust-for-linux/0 rust-for-linux/git/0.git

public-inbox-init -V2 --ng org.kernel.vger.rust-for-linux \
    rust-for-linux ./rust-for-linux http://lore.kernel.org/rust-for-linux \
    rust-for-linux@vger.kernel.org
public-inbox-index ./rust-for-linux
```

## analyze emails

```bash
# python3 title.py # get all the emails titles
# python3 email_time.py # get the sum emails counts-time
# python3 analyze.py # get the emails counts-time
# python3 class.py # get the classifaction
python3 split.py # add time and title in a file
python3 even_class.py # get the classifactions
```

-----------------------------------------------------------
safety_abstraction length is  39
drivers length is  40
build length is  122
bugs length is  6
docs length is  15
rust length is  0
linux length is  0
questions length is  44
others length is  376
-----------------------------------------------------------
-----------------------------------------------------------
safety_abstraction length is  77
drivers length is  46
build length is  144
bugs length is  6
docs length is  22
rust length is  0
linux length is  0
questions length is  48
others length is  413
-----------------------------------------------------------
-----------------------------------------------------------
safety_abstraction length is  102
drivers length is  61
build length is  199
bugs length is  6
docs length is  38
rust length is  0
linux length is  0
questions length is  48
others length is  466
-----------------------------------------------------------
-----------------------------------------------------------
safety_abstraction length is  195
drivers length is  97
build length is  303
bugs length is  8
docs length is  88
rust length is  4
linux length is  0
questions length is  48
others length is  509
-----------------------------------------------------------
-----------------------------------------------------------
safety_abstraction length is  419
drivers length is  116
build length is  437
bugs length is  21
docs length is  96
rust length is  19
linux length is  6
questions length is  48
others length is  539
-----------------------------------------------------------
-----------------------------------------------------------
safety_abstraction length is  1040
drivers length is  202
build length is  507
bugs length is  31
docs length is  117
rust length is  174
linux length is  14
questions length is  48
others length is  644
-----------------------------------------------------------
-----------------------------------------------------------
safety_abstraction length is  1436
drivers length is  384
build length is  595
bugs length is  35
docs length is  124
rust length is  192
linux length is  15
questions length is  48
others length is  677
-----------------------------------------------------------


## plot the result

```bash
python3 new_plt.py
```