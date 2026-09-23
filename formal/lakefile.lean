import Lake
open Lake DSL

package «gss2012» where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.19.0"

@[default_target]
lean_lib «Gss2012» where
