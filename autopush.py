import os
import subprocess

# Variables
REPO_DIR = r"D:\learngit"  # Path to your repository
REMOTE_URL = "https://github.com/mrvincenzo004/newrepo.git"  # URL of your repository
BRANCH_NAME = "master"  # Branch name to push to
COMMIT_MESSAGE = "auto commit"  # Commit message
GIT_USER_NAME = "mrvincenzo004"  # Your GitHub username
GIT_USER_EMAIL = "mrvincenzo33@gmail.com"  # Your GitHub email

def run_command(command, cwd=None):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Command failed with error:\n{result.stderr}")
        exit(1)
    return result.stdout

def push_changes():
    os.chdir(REPO_DIR)

    # Set Git user name and email
    run_command(f'git config --global user.name "{GIT_USER_NAME}"')
    run_command(f'git config --global user.email "{GIT_USER_EMAIL}"')

    # Check if .git directory exists
    if not os.path.isdir(".git"):
        print("Initializing a new Git repository...")
        run_command("git init")
    else:
        print("Git repository already initialized.")

    # Add changes to staging
    run_command("git add .")

    # Check if remote URL is already added
    remotes = run_command("git remote").split()
    if "origin" in remotes:
        print("Remote URL already added.")
    else:
        print("Adding remote URL...")
        run_command(f"git remote add origin {REMOTE_URL}")

    # Commit changes
    run_command(f'git commit -m "{COMMIT_MESSAGE}"')

    # Push to the repository
    run_command(f"git push -u origin {BRANCH_NAME}")

if __name__ == "__main__":
    push_changes()
