# Python ADTs Mastery

**Python ADTs Mastery** is a collection of implementations and examples of Abstract Data Types (ADTs) in Python, designed to help you deeply understand and master fundamental data structures and algorithms. This project covers queues, stacks, linked lists, trees, graphs, and more, with code samples, tests, benchmarks, and visualizations.

---

## Table of Contents

1. [Features](#features)
2. [Technologies](#technologies)
3. [Getting Started](#getting-started)

   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
4. [Usage](#usage)
5. [Testing and Quality](#testing-and-quality)
6. [Profiling and Benchmarking](#profiling-and-benchmarking)
7. [Docker & CI](#docker--ci)
8. [Project Structure](#project-structure)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features

* **Implementations of core ADTs**: Stack, Queue, LinkedList, BinaryTree, Graph, etc.
* **Unit tests** with `pytest` and coverage reporting.
* **Code style & linting**: Automated formatting with `black`, lint checks with `flake8` and `pylint`.
* **Profiling tools**: `memory-profiler`, `line-profiler`, `py-spy` for performance analysis.
* **Benchmarks** using `pytest-benchmark` to compare implementations.
* **Data analysis & visualization**: Examples using `numpy`, `pandas`, and `matplotlib`.
* **Dockerized CI environment** for reproducible builds and testing.
* **Git Flow** workflow for structured branching and release management.

---

## Technologies

* **Language**: Python 3.12 (managed with `pyenv`)
* **Testing**: `pytest`, `pytest-cov`, `pytest-benchmark`
* **Linting & Formatting**: `black`, `flake8`, `pylint`
* **Profiling**: `memory-profiler`, `line-profiler`, `py-spy`
* **Data**: `numpy`, `pandas`, `matplotlib`
* **Containers**: Docker (`Dockerfile`, `docker-compose.yml`)
* **CI/CD**: GitHub Actions
* **Branching**: Git Flow (`git-flow`)

---

## Getting Started

### Prerequisites

* Python 3.12 installed via `pyenv`
* `pyenv-virtualenv` plugin (optional but recommended)
* Docker and Docker Compose (for CI environment)
* Git and `git-flow`

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-user/python-adts-mastery.git
   cd python-adts-mastery
   ```
2. **Set up Python environment**:

   ```bash
   pyenv install 3.12.10
   pyenv virtualenv 3.12.10 python-adts-mastery
   pyenv activate python-adts-mastery
   ```
3. **Install runtime dependencies**:

   ```bash
   pip install numpy pandas matplotlib
   ```
4. *(Optional)* **Install dev tools locally**:

   ```bash
   pip install black flake8 pylint pytest pytest-cov pytest-benchmark memory-profiler line-profiler py-spy
   ```

---

## Usage

* Import and use ADT implementations in your scripts or REPL.
* Example:

  ```python
  from adts.queue import Queue

  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  print(q.dequeue())  # 1
  ```
* See `examples/` directory for more usage scenarios and Jupyter notebooks.

---

## Testing and Quality

* **Run tests**:

  ```bash
  pytest
  ```
* **View coverage report**:

  ```bash
  pytest --cov=adts --cov-report=html
  ```
* **Formatting & linting**:

  ```bash
  black --check .
  flake8 .
  pylint adts/
  ```

---

## Profiling and Benchmarking

* **Memory profiling**:

  ```bash
  mprof run script.py
  mprof plot
  ```
* **Line profiling**:

  ```bash
  kernprof -l -v script.py
  ```
* **Sampling profiler**:

  ```bash
  py-spy record -o profile.svg -- python script.py
  ```
* **Benchmarks**:

  ```bash
  pytest --benchmark-only
  ```

---

## Docker & CI

* **Build Docker image**:

  ```bash
  docker build -t python-ci-env .
  ```
* **Run commands in container**:

  ```bash
  docker run --rm -v $(pwd):/app python-ci-env black .
  docker run --rm -v $(pwd):/app python-ci-env pytest
  ```
* **Docker Compose**:

  ```bash
  docker-compose run --rm ci pytest
  docker-compose run --rm ci flake8 .
  ```
* **GitHub Actions**: See `.github/workflows/ci.yml` for pipeline configuration.

---

## Project Structure

├── src/
├── docs/
├── tests/
├── examples/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .github/workflows/ci.yml
├── README.md
└── LICENSE
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git flow feature start my-feature`
3. Commit changes and run tests locally
4. Push to your fork and open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
