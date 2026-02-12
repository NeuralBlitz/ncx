# 🔧 Setup Guide for NeuralBlitz Buggy Server Data

## 🚨 Problem: Invalid Path Issues After Git Clone

When you clone this repository, you may encounter Python path issues and syntax errors that prevent the code from running properly.

## 🛠️ Solution: Automated Setup

Run the provided setup script to fix all common issues:

```bash
python setup.py
```

## ✅ What the Setup Script Fixes

### 1. **Python Path Issues**
- Adds correct paths to `sys.path` for relative imports
- Fixes import errors for modules like `sss_ref` and `morphspec_runner`

### 2. **Syntax Errors**
- Fixes missing commas in function arguments
- Corrects f-string formatting issues  
- Resolves unterminated string literals
- Fixes bracket mismatches

### 3. **Dependency Validation**
- Checks for required packages (numpy, psutil, etc.)
- Reports missing dependencies with installation guidance

### 4. **Demo Verification**
- Runs a test to ensure the setup works
- Generates sample output files to verify functionality

## 📁 Key Files Fixed

| File | Issue | Fix |
|------|-------|-----|
| `alembic/versions/2026_02_09_1245-005_seed_data.py` | f-string brace issue | Added proper f-string formatting |
| `comprehensive_benchmark_suite.py` | Function definition error | Fixed class method indentation |
| `comprehensive_benchmark_suite_fixed.py` | Missing commas | Added missing commas in function calls |
| `comprehensive_performance_baseline.py` | Missing commas | Added missing commas in function calls |
| `comprehensive_performance_baseline_fixed.py` | Empty f-string | Fixed f-string expression |
| `comprehensive_quantum_validation_report.py` | Unterminated string | Removed stray quote character |
| `consolidate_docs.py` | Invalid string formatting | Fixed format string syntax |

## 🧪 Manual Verification

After running the setup script, you can verify everything works:

```bash
# Navigate to the main demo directory
cd buggy/server/data/Python/NeuralBlitzzz

# Run the demo
python demo_run.py

# Check for generated files
ls -la session_v1.ostph.json morph_result.json
```

## 🔍 Manual Fix Checklist

If you prefer to fix issues manually, check these:

### Python Imports
```python
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
```

### Common Syntax Issues
1. **Missing commas in function calls:**
   ```python
   # Wrong
   func(arg1=value1
        arg2=value2)
   
   # Right
   func(arg1=value1,
        arg2=value2)
   ```

2. **F-string formatting:**
   ```python
   # Wrong
   f"Hello {}" .format(name)
   
   # Right
   f"Hello {name}"
   ```

3. **Unmatched brackets/quotes:**
   ```python
   # Wrong
   print("unclosed string
   
   # Right
   print("closed string")
   ```

## 📦 Dependencies

The setup script validates these dependencies are available:

- ✅ numpy - For numerical computations
- ✅ psutil - For system monitoring  
- ✅ typing_extensions - For type hints
- ✅ pydantic - For data validation
- ✅ fastapi - For API framework
- ✅ uvicorn - For ASGI server

If any are missing, install them:
```bash
pip install numpy psutil typing_extensions pydantic fastapi uvicorn
```

## 🎯 Success Indicators

When setup is successful, you should see:

```
🎉 Setup completed successfully!
💡 You can now run:
   cd buggy/server/data/Python/NeuralBlitzzz
   python demo_run.py
```

And the demo should generate:
- `session_v1.ostph.json` - Session bundle with SSS and morphological data
- `morph_result.json` - Results from morphological computation

## 🐛 Troubleshooting

### Import Errors Still Occur
1. Check your current working directory
2. Ensure you're running Python from the correct location
3. Verify the setup script completed without errors

### Demo Fails to Run
1. Check if all dependencies are installed
2. Verify file permissions on Python files
3. Check for any remaining syntax errors with:
   ```bash
   python -m py_compile buggy/server/data/Python/NeuralBlitzzz/demo_run.py
   ```

### Generated Files Missing
1. Check if you have write permissions in the directory
2. Verify the demo ran to completion
3. Look for any error messages in the console output

## 📞 Getting Help

If you continue to experience issues:

1. **Check the setup output** - All errors are logged with specific file paths
2. **Run individual tests** - Test imports and files one by one
3. **Verify Python version** - Ensure you're using Python 3.8+
4. **Check system permissions** - Ensure write access to generate output files

The setup script is designed to handle the most common issues that occur when cloning this repository from GitHub.