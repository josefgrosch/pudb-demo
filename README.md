# pudb-demo

---
## Helpful links

 - [pudb cheat sheet](https://bit.ly/3lN4kmF)

 - [This demo's code](https://github.com/josefgrosch/pudb-demo)

 - [pydb web site](https://pypi.org/project/pudb/)

 - [pudb documentation](https://documen.tician.de/pudb/)

 ---
 ## Installing pudb

### New Install
  - sudo apt update
  - sudo apt dist-upgrade -y
  - sudo apt install python3-pip
  - pip install pudb

### Update python and pip
 - pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
 - pip install pudb

 ---

## Enable on the fly debugging
 - Only work with python 3.7 and newer.
 - Insert the following into ~/.bashrc

```export PYTHONBREAKPOINT="pudb.set_trace"```
