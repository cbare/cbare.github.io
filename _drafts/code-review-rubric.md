

Is new code covered by tests?

Look for repetition. DRY.

Does this PR add code-debt?


Following existing patterns that are bad?
Not following existing patterns that are good?

Using appropriate standard library components, not reinventing the wheel
Using appropriate re-usable components, not reinventing the wheel


- clarity, readability, naming, comments
- efficiency
  - choice of data structures
  - memory and cpu usage
  - repeating work
- complexity, simpler is better
- testing
  - reasonable test coverage: happy path and edge cases
  - is code factored into small simple testable units?
- increase technical de


Look for trade-offs


A simpler implementation will allow us to deploy working code and start getting feedback sooner. We can always iterate based on feedback to fix rough spots and add features.

