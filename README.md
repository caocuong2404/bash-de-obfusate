# Bash de-obfuscate (obfuscated by [node bash-obfuscate](https://www.npmjs.com/package/bash-obfuscate))

Scripts de-obfuscation by node bash-obfuscate

## Getting Started

- **bash-de-obfuscate** is a tools de-obfuscate a bash file has been obfuscate by **bash-obfuscate**.
- **bash-obfuscate** is a node.js CLI tool and library to heavily obfuscate bash scripts.

### Prerequisites

![python-badge](https://img.shields.io/badge/python-3.x.x-blue)

- [Python 3.x.x](https://www.python.org/downloads/)
- [Argparse module](https://pypi.org/project/argparse/)

### Installing

Clone repo to your computer.

```
git clone https://github.com/caocuong2404/bash-de-obfuscate.git
```

## Guides

### Help

```bash
python main.py -h
```

### De-obfuscate bash file

```bash
python main.py -i input.install -o output.sh
```

<!-- or simple command :)
cat input.sh | sed 's/eval/echo/' | sh > output.sh && cat output.sh
-->

## Versioning

```bash
python main.py -v
```

## Authors

**Peter James** - [CaoCuong2404](https://github.com/CaoCuong2404)

See also the list of [contributors](https://github.com/caocuong2404/bash-de-obfuscate/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
