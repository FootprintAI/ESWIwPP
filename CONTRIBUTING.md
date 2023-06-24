# Contributing to ESWIwPP(Enhancing Social Welfare Issues with Public Participation)

We want to make contributing to this project as easy and transparent as possible.

## TL;DR

We appreciate all contributions. If you are interested in contributing to ESWIwPP, there are many ways to help out.
Your contributions may fall into the following categories:

- It helps the project if you can

  - Report issues that you're facing
  - Give a :+1: on issues that others reported and that are relevant to you

- Answering questions on the issue tracker, investigating bugs are very valuable contributions to the project.

- You would like to improve the documentation. This is no less important than improving the library itself! If you find
  a typo in the documentation, do not hesitate to submit a GitHub pull request.

- If you would like to fix a bug:

  - comment on the issue that you want to work on this issue
  - send a PR with your fix, see below.

- If you plan to contribute new features, utility functions or extensions, please first open an issue and discuss the
  feature with us.
  - We have a checklist of things to go through while adding a new DataPipe. See below.
- If you would like to feature a usage example in our documentation, discuss that with us in an issue.

## Issues

We use GitHub issues to track public bugs. Please follow the existing templates if possible and ensure that the
description is clear and has sufficient instructions to be able to reproduce the issue.

## Pull Requests

We actively welcome your pull requests.

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation and examples.
4. Ensure the test suite passes.
5. If you haven't already, complete the Contributor License Agreement ("CLA").

### Code style

`ESWIwPP` enforces a fairly strict code format through [`pre-commit`](https://pre-commit.com). You can install it with

```shell
pip install pre-commit
```

or

```shell
conda install -c conda-forge pre-commit
```

To check and in most cases fix the code format, stage all your changes (`git add`) and run `pre-commit run`. To perform
the checks automatically before every `git commit`, you can install them with `pre-commit install`.

## Contributor License Agreement ("CLA")

TODO...

## License

By contributing to ESWIwPP, you agree that your contributions will be licensed under the LICENSE file in the root
directory of this source tree.
