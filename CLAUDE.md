# ha-ci-testing

Throwaway integration whose only purpose is exercising the CI and release pipeline the
`ha-integration` skill ships. Nothing here is meant to run on someone's Home Assistant.

## AI sessions

Before writing or modifying integration code (config flow, platforms, manifest,
websocket, services…), invoke the `ha-integration` skill. Re-invoke it after any
`/compact`, since compaction can drop the skill's guidance from context.

## Enable the commit hook once per clone

```
git config core.hooksPath .githooks
```
