with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The OLD JS block starts exactly at '// ── CALCULATOR ──'
# We need to find the START of the old block (which currently is still there).
start_idx = html.find('// ── CALCULATOR ──')
if start_idx != -1:
    # Now we need to find the end of the new JS block we inserted, or rather, where the old JS was supposed to end.
    # Actually, because we already inserted new_js, the file currently has:
    # [old JS part 1: CALCULATOR_THEMES to calculateCalcValues]
    # [old JS part 2: openCalc to calcBeep]
    # ... Wait, my previous script started replacing at `let CALC_CURRENT='0'`.
    # So `let CALC_CURRENT='0'` (old one) was removed, along with `handleCalcKey`, `toggleCalculatorPalette`, `setCalculatorTheme`.
    # And replaced with the ENTIRE `new_js`.
    # So right now we have:
    # 1. `const CALCULATOR_THEMES=` (old)
    # 2. `openCalc()` (old)
    # 3. `new_js` (which contains NEW CALCULATOR_THEMES, etc.)
    # We should delete the old JS that we missed.
    pass
