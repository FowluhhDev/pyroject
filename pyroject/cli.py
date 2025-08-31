# pyroject/cli.py
import json, subprocess, sys, os, shlex

PROJECT_FILE = os.path.join(os.getcwd(), "project.json")

def install_dependencies():
    """Install all dependencies from project.json."""
    if not os.path.exists(PROJECT_FILE):
        print(f"{PROJECT_FILE} not found.")
        return
    with open(PROJECT_FILE) as f:
        config = json.load(f)
    deps = config.get("dependencies", {})
    if not deps:
        print("No dependencies found in project.json.")
        return
    print("Installing dependencies...")
    for pkg, version in deps.items():
        subprocess.run([sys.executable, "-m", "pip", "install", f"{pkg}{version}"])

def run_script(script_name):
    """Run a script from project.json in a cross-platform way."""
    if not os.path.exists(PROJECT_FILE):
        print(f"{PROJECT_FILE} not found.")
        return
    with open(PROJECT_FILE) as f:
        config = json.load(f)
    scripts = config.get("scripts", {})
    if script_name not in scripts:
        print(f"Script '{script_name}' not found. Available: {', '.join(scripts)}")
        return

    command = scripts[script_name]

    # If it's a Python command, replace 'python' with sys.executable
    if command.startswith("python "):
        parts = shlex.split(command)
        parts[0] = sys.executable
        subprocess.run(parts)
    else:
        # Generic shell command
        subprocess.run(command, shell=True)

def install_package(package_name):
    """Install a single package from pip."""
    subprocess.run([sys.executable, "-m", "pip", "install", package_name])

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  pyroject install             # Install dependencies from project.json")
        print("  pyroject run <script>        # Run a script from project.json")
        print("  pyroject pip-install <name>  # Install a package from pip")
        return

    action = sys.argv[1]

    if action == "install":
        install_dependencies()
    elif action == "run":
        if len(sys.argv) < 3:
            print("Please specify a script name.")
            return
        run_script(sys.argv[2])
    elif action == "pip-install":
        if len(sys.argv) < 3:
            print("Please specify a package name.")
            return
        install_package(sys.argv[2])
    else:
        print(f"Unknown action '{action}'")

if __name__ == "__main__":
    main()