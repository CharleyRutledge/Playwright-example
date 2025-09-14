#!/usr/bin/env python3
"""
Allure Report Generator
Generate and serve Allure reports for Playwright tests.
"""

import subprocess
import sys
import os
from pathlib import Path


def check_allure_installed():
    """Check if Allure command line tool is installed."""
    try:
        subprocess.run(["allure", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def install_allure():
    """Install Allure command line tool."""
    print("Installing Allure command line tool...")
    try:
        # Try to install via npm
        subprocess.run(["npm", "install", "-g", "allure-commandline"], check=True)
        print("✅ Allure installed successfully via npm")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Failed to install Allure via npm")
        print("Please install Allure manually:")
        print("1. Download from: https://github.com/allure-framework/allure2/releases")
        print("2. Or install via package manager (choco, brew, etc.)")
        return False


def generate_report():
    """Generate Allure report from results."""
    results_dir = Path("allure-results")
    
    if not results_dir.exists() or not list(results_dir.glob("*.json")):
        print("❌ No Allure results found. Run tests first:")
        print("   pytest tests/ -v")
        return False
    
    print("📊 Generating Allure report...")
    try:
        # Generate static report
        subprocess.run([
            "allure", "generate", 
            str(results_dir), 
            "--clean", 
            "-o", "allure-report"
        ], check=True)
        print("✅ Allure report generated in 'allure-report/' directory")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to generate report: {e}")
        return False


def serve_report():
    """Serve Allure report locally."""
    results_dir = Path("allure-results")
    
    if not results_dir.exists() or not list(results_dir.glob("*.json")):
        print("❌ No Allure results found. Run tests first:")
        print("   pytest tests/ -v")
        return False
    
    print("🌐 Starting Allure report server...")
    print("📱 Report will be available at: http://localhost:8080")
    print("⏹️  Press Ctrl+C to stop the server")
    
    try:
        subprocess.run(["allure", "serve", str(results_dir)], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to serve report: {e}")
        return False
    
    return True


def open_report():
    """Open generated Allure report in browser."""
    report_dir = Path("allure-report")
    
    if not report_dir.exists():
        print("❌ No report found. Generate report first:")
        print("   python generate_allure_report.py generate")
        return False
    
    print("🌐 Opening Allure report in browser...")
    try:
        subprocess.run(["allure", "open", str(report_dir)], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to open report: {e}")
        return False


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Allure Report Generator")
        print("=" * 30)
        print("Usage:")
        print("  python generate_allure_report.py serve    # Serve report locally")
        print("  python generate_allure_report.py generate # Generate static report")
        print("  python generate_allure_report.py open     # Open generated report")
        print("  python generate_allure_report.py install  # Install Allure CLI")
        return
    
    command = sys.argv[1].lower()
    
    if command == "install":
        if not check_allure_installed():
            install_allure()
        else:
            print("✅ Allure is already installed")
    
    elif command == "serve":
        if not check_allure_installed():
            print("❌ Allure not installed. Run 'python generate_allure_report.py install' first")
            return
        serve_report()
    
    elif command == "generate":
        if not check_allure_installed():
            print("❌ Allure not installed. Run 'python generate_allure_report.py install' first")
            return
        generate_report()
    
    elif command == "open":
        if not check_allure_installed():
            print("❌ Allure not installed. Run 'python generate_allure_report.py install' first")
            return
        open_report()
    
    else:
        print(f"❌ Unknown command: {command}")
        print("Available commands: serve, generate, open, install")


if __name__ == "__main__":
    main()
