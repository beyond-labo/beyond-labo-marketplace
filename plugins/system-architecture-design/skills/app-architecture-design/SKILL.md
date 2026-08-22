---
name: app-architecture-design
description: Design or review client application architecture for a new screen, feature, flow, or refactor. Use for feature-first package boundaries, View/ViewModel/UseCase design, UI state and navigation ownership, Clean Architecture dependency direction, ports and adapters, and application package naming.
---

# App Architecture Design

Design a client application so its UI state, feature ownership, dependency direction, and platform boundaries remain clear as it evolves. Apply this skill to frontend, mobile, desktop, and other user-facing application code; use `backend-architecture-design` for server-side APIs and services.

## Workflow

1. Read the repository's local architecture, package, and UI-framework guidance before proposing a structure. Treat local rules as more specific than this skill.
2. Identify the smallest user-facing feature that can change and be tested independently. Make its screen contract, UI state, user actions, use cases, navigation boundary, and external effects explicit.
3. Use the feature as the package root. Keep its layers inside the feature rather than distributing new code by technical type across the application.
4. Place each component by its dependency and responsibility, then select a name and role directory that reveal both.
5. Record the feature boundary, layer/role placement, cross-feature contracts, UI-state ownership, and intentional exceptions in the design or specification.
6. Review imports, state ownership, composition, tests, and public contracts before implementation.

## Boundaries and dependency direction

Use these conceptual layers when they fit the application:

| Layer | Owns | May depend on |
| --- | --- | --- |
| Domain | business concepts, invariants, policies, value types | no UI framework or external SDK |
| Application | use cases, orchestration, input/output types, ports | domain abstractions |
| Infrastructure | storage, network clients, SDKs, providers, port implementations | application/domain contracts |
| Presentation | views, view models, UI state, UI mappers, platform controllers | application APIs and platform UI APIs |
| Composition | dependency wiring, root navigation registration | all layers; no business rules |

Distinguish runtime flow from static imports.

- Runtime flow is normally `View -> (platform controller) -> ViewModel -> UseCase -> Port -> Adapter -> Store / external API`.
- Static imports flow toward stable abstractions: `presentation -> application -> domain`, `infrastructure -> application/domain`, and `composition -> all layers`.
- A platform controller is optional. Use it only for a framework-required lifecycle, navigation, or platform API boundary; state-driven Views may bind directly to a ViewModel.

Let Composition inject concrete adapters into use cases and view models. Do not construct a concrete Adapter, repository, store, HTTP client, or SDK client from a ViewModel, UseCase, or Domain component. Define a Port where its caller needs the abstraction—normally Application, or Domain when the domain truly owns the capability—and implement it in Infrastructure.

Do not make Domain or Application import a UI framework, View type, screen state, navigation API, browser API, database driver, network client, or provider SDK. Do not put business rules in a View, platform controller, or navigation callback.

Use an explicit contract when features communicate. Do not import another feature's Presentation or Infrastructure implementation. Move code to a shared kernel only when it is a stable, owned application/domain contract used by multiple features; do not create `common`, `shared`, `lib`, or utility dumping grounds for convenience.

## Package and naming design

For new feature work, use this shape and omit only layers that have no responsibility:

```text
src/<feature-name>/<clean-architecture-layer>/<role-name>/<type>
```

For example:

```text
src/Matching/Presentation/View/MatchingMainView
src/Matching/Presentation/ViewModel/MatchingMainViewModel
src/Matching/Presentation/Mapper/MatchingMainUiMapper
src/Matching/Application/UseCase/FindAvailableMatches
src/Matching/Application/Port/MatchingRepository
src/Matching/Domain/Model/Availability
src/Matching/Domain/Service/MatchingPolicy
src/Matching/Infrastructure/Adapter/FirestoreMatchingRepository
src/Matching/Infrastructure/Store/FirestoreMatchingStore
src/Matching/Composition/Factory/MatchingFeatureFactory
```

Use role directories even when they initially contain one component, unless the design documents why an exception improves discoverability. Use names that expose both responsibility and layer role: `*View`, `*ViewModel`, `*UiState`, `*Controller`, `*Mapper`, `*UseCase`, `*Port`, `*Policy`, `*Adapter`, `*Repository`, `*Store`, `*Client`, and `*Factory`. Avoid catch-all names such as `Manager`, `Helper`, `Util`, and generic `Processor`.

A Repository is a feature-facing persistence/data-access abstraction or its implementation; an Adapter translates between a Port and an external system; a Store is a lower-level persistence, cache, or transport mechanism. Do not use the names interchangeably merely because they all access data.

## Design checks

Before implementation, verify that:

- The feature owns one coherent user-facing capability, screen/flow contract, and UI state.
- Each new type has a feature, layer, and role directory matching `<Feature>/<Layer>/<Role>/<Type>`.
- A View delegates actions and rendering state; its ViewModel owns presentation state; a UseCase owns application orchestration.
- A ViewModel calls a UseCase rather than a Repository, Store, HTTP client, database, or SDK directly.
- Domain has no framework or I/O dependency, and Application has no concrete Infrastructure dependency.
- External effects cross a Port and Adapter or another explicit contract; Composition performs the concrete wiring.
- Navigation and platform lifecycle code remain at Presentation/Composition boundaries and do not contain business decisions.
- Shared concepts have an owner; reuse does not conceal a feature dependency or create a cycle.
- Tests cover user-visible behavior at the Presentation/Application boundary and contracts at Infrastructure seams.
- The design distinguishes an additive feature from a deliberate migration or refactor.

When updating an existing application, preserve current placement unless migration is in scope. State the exception, its reason, and the target boundary for every new element; use a mapper or anti-corruption adapter at a legacy boundary rather than widening an incorrect dependency.
