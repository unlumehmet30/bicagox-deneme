# bicagox-deneme

Synthetic OpenAPI and TypeScript fixture for the Bicagox contract checker.
The review workflow runs in static mode for this test.

- Base contract returns a numeric amount.
- The regression commit permits a null amount while the client still calls
  toFixed on it.
- The follow-up commit handles null before formatting.

The nullability finding should appear on the regression commit and disappear
after the follow-up. The policy check tracks the verified finding.

The engine is checked out from unlumehmet30/bicagox at a pinned commit.
