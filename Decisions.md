## Decision: Service layer

Context: Separate logic
Options: Inline vs service
Choice: Service
Why: Testability

## Decision: In-memory store

Context: Simplicity
Options: DB vs in memory
Choice: In Memory
Why: Requirement

## Decision: Modular routes

Context: Scaling
Options: Single router vs Modular router
Choice: Modular routers
Why: Clean structure

## Decision: UUID ids

Context: IDs for objects
Options: numerical vs uuid
Choice: UUID
Why: Unique ids instead of numerical ids, UUIDs are more secure

## Decision: Manual discount trigger

Why: Control

## Decision: No Authentication

Why: Simplicity and no explicit mention in the problem statement
