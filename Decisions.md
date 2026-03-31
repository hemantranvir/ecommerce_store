## Decision: Service layer

Context: Separate logic
Options: Inline vs service
Choice: Service
Why: Testability

## Decision: In-memory store

Context: Simplicity
Choice: Memory
Why: Requirement

## Decision: Modular routes

Context: Scaling
Choice: Split routers
Why: Clean structure

## Decision: UUID ids

Why: Unique ids instead of numerical ids, UUIDs are more secure

## Decision: Manual discount trigger

Why: Control

## Decision: No Authentication

Why: Simplicity and no explicit mention in the problem statement
