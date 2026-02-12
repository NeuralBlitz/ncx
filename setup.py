#!/usr/bin/env python3
"""
Setup script for NeuralBlitz Buggy Server Data
Fixes common path and syntax issues after git clone
"""

import os
import sys
import subprocess
import json
from pathlib import Path


def check_python_version():
    """Check if Python 3.8+ is available"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required, found:", sys.version)
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True


def install_dependencies():
    """Check if required dependencies are available"""
    print("📦 Checking dependencies...")

    # Core dependencies
    deps = ["numpy", "psutil", "typing_extensions", "pydantic", "fastapi", "uvicorn"]

    for dep in deps:
        try:
            __import__(dep)
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ⚠️  {dep} not available (may need to install manually)")


def fix_path_issues():
    """Fix common Python path issues"""
    current_dir = Path(__file__).parent.absolute()
    python_paths = [
        current_dir / "buggy" / "server" / "data" / "Python",
        current_dir / "buggy" / "server" / "data" / "Python" / "NeuralBlitzzz",
        current_dir / "server" / "data" / "Python",
        current_dir / "server" / "data" / "Python" / "NeuralBlitzzz",
    ]

    for path in python_paths:
        if path.exists():
            if str(path) not in sys.path:
                sys.path.insert(0, str(path))
                print(f"  ✅ Added to Python path: {path}")


def test_imports():
    """Test critical imports"""
    print("🧪 Testing imports...")

    test_files = [
        "buggy/server/data/Python/NeuralBlitzzz/sss_ref.py",
        "buggy/server/data/Python/NeuralBlitzzz/morphspec_runner.py",
        "buggy/server/data/Python/NeuralBlitzzz/demo_run.py",
    ]

    for test_file in test_files:
        try:
            # Test syntax by compiling
            with open(test_file, "r") as f:
                compile(f.read(), test_file, "exec")
            print(f"  ✅ {test_file}")
        except Exception as e:
            print(f"  ❌ {test_file}: {e}")


def run_demo():
    """Run demo to verify setup"""
    print("🚀 Running demo...")

    demo_path = Path("buggy/server/data/Python/NeuralBlitzzz/demo_run.py")
    if demo_path.exists():
        try:
            # Use absolute path
            result = subprocess.run(
                [sys.executable, str(demo_path.absolute())],
                capture_output=True,
                text=True,
                cwd=demo_path.parent.absolute(),
            )
            if result.returncode == 0:
                print("  ✅ Demo completed successfully")
                print(f"  📄 Generated: session_v1.ostph.json")
                return True
            else:
                print(f"  ❌ Demo failed: {result.stderr}")
                return False
        except Exception as e:
            print(f"  ❌ Demo error: {e}")
            return False
    else:
        print("  ❌ Demo file not found")
        return False


def create_gitignore():
    """Create proper .gitignore if missing"""
    gitignore_path = Path(".gitignore")
    if not gitignore_path.exists():
        gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific
*.log
session_v1.ostph.json
morph_result.json
.pytest_cache/
"""
        with open(gitignore_path, "w") as f:
            f.write(gitignore_content.strip())
        print("  ✅ Created .gitignore")


def main():
    """Main setup routine"""
    print("🔧 NeuralBlitz Setup starting...")
    print("=" * 50)

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    # Install dependencies
    install_dependencies()

    # Fix path issues
    fix_path_issues()

    # Test imports
    test_imports()

    # Create gitignore
    create_gitignore()

    # Run demo
    demo_success = run_demo()

    print("=" * 50)
    if demo_success:
        print("🎉 Setup completed successfully!")
        print("💡 You can now run:")
        print("   cd buggy/server/data/Python/NeuralBlitzzz")
        print("   python demo_run.py")
    else:
        print("❌ Setup completed with errors. Check the output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
