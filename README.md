# ha-ci-testing

Throwaway Home Assistant integration used to exercise the `ha-integration` skill's CI
and release pipeline against a real repository: real releases, real zip assets, real
release notes. It implements no device support and should never be installed. Its
workflows are callers of `release-flow` and `ha-integration-ci`; what each does is
those repositories' READMEs.

A throwaway repo: releases here are test artefacts, not software anyone should install.
