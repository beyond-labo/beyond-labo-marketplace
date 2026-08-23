---
name: backend-architecture-design
description: Design or review backend architecture for a new feature, API, service, or refactor. Use for feature-first package boundaries, Clean Architecture or layered architecture, dependency direction, ports and adapters, naming, shared-kernel decisions, and architecture sections of specifications.
---

# Backend Architecture Design

Design a backend so that its feature ownership, dependency direction, and operational boundaries remain clear as it evolves.

## Workflow

1. Read the repository's local architecture, package, and specification guidance before proposing a structure. Treat local rules as more specific than this skill.
2. Identify the smallest feature that can change and be tested independently. Make its public contract, owned data, use cases, and external dependencies explicit.
3. Use the feature as the package root. Keep its layers inside the feature rather than distributing new code by technical type across the service.
4. Place each component by its dependency and responsibility, then select a name and role directory that reveal both.
5. Record the feature boundary, layer/role placement, cross-feature contracts, and intentional exceptions in the design or specification.
6. Review imports, ownership, tests, and public contracts before implementation.

## Boundaries and dependency direction

Use these conceptual layers when they fit the system:

| Layer | Owns | May depend on |
| --- | --- | --- |
| Domain | business concepts, invariants, policies, value types, ports | no delivery framework or external SDK |
| Application | use cases and orchestration | domain abstractions |
| Infrastructure | databases, messaging, SDKs, providers, port implementations | domain contracts |
| Presentation | transport validation, handlers/routes, response projection | application APIs |
| Composition | dependency wiring | all layers; no business rules |

Keep imports flowing toward stable abstractions: `presentation -> application -> domain` and `infrastructure -> domain`. Let composition wire concrete infrastructure to ports. Do not make a domain or application component import a transport framework, database driver, provider SDK, or a feature's presentation code.

Use an explicit contract when features or services communicate. Do not import another feature's infrastructure or presentation implementation.

Move code into a shared kernel only when it is a stable, owned domain contract used by multiple features. Do not create `common`, `shared`, `lib`, or utility dumping grounds for convenience.

## Package and naming design

For new feature work, prefer this shape and omit only layers that have no responsibility:

```text
src/<feature-name>/<layer-name>/<role-name>/
```

Use role directories that match the component's responsibility, such as `entities`, `policies`, `ports`, `use-cases`, `orchestrators`, `adapters`, `repositories`, `routes`, `handlers`, or `projectors`. Place composition code in a role directory too: use `composition/factories/` for object graphs and `composition/registrars/` for registration-only wiring.

Use names that expose the layer and role: `*Policy`, `*Port`, `*UseCase`, `*Orchestrator`, `*Adapter`, `*Repository`, `*Provider`, `*Route`, `*Handler`, `*Mapper`, and `*Projector`. Reserve `*Emitter` for a component that actually pushes to an external channel. Avoid catch-all names such as `Manager`, `Helper`, `Util`, and generic `Processor`.

Use a role directory even when it initially contains one component, unless the design documents why an exception improves discoverability. This applies to composition as well as the four architectural layers. Do not move existing code solely to conform; give a migration its own approved refactoring scope.

## Design checks

Before implementation, verify that:

- The feature owns one coherent capability and its public contract is named.
- Each new file has a feature, layer, and role directory.
- The domain has no framework or I/O dependency, and the application has no concrete infrastructure dependency.
- External effects cross an adapter, port, or explicit contract.
- Shared concepts have an owner; reuse does not conceal a feature dependency.
- Tests exercise behavior at the feature boundary and contracts at integration seams.
- The design distinguishes an additive feature from a deliberate migration/refactor.

When updating an existing specification, preserve the current placement unless migration is in scope. State the exception, its reason, and the target boundary for every new element.
