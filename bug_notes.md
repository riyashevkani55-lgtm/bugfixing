# Bug Notes & Debugging Summary

| Bug | Evidence / Failed Test | Root Cause | Implemented Fix |
| :--- | :--- | :--- | :--- |
| **Average Calculation** | `135.0 != 90.0`; `ZeroDivisionError` on single mark | Denominator was `len(marks) - 1`, which divides by 0 for single items and distorts multi-mark averages | Changed denominator to `len(marks)` |
| **Pass Boundary** | `is_passing(40)` returned `False` | Condition used strict inequality (`>`) instead of inclusive inequality (`>=`) | Updated condition to `mark >= PASS_MARK` |
| **Grade Ordering** | `get_grade(95)` returned `"First"` | Branch `average >= 60` was evaluated before `average >= 90`, shadowing the Distinction tier | Reordered checks: evaluate `>= 90` first, followed by `>= 60` and `>= 45` |
