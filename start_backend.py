#!/usr/bin/env python3
"""
Backend startup script for MCP Chat
Installs dependencies and starts the server
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required Python packages"""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def start_server():
    """Start the Flask server"""
    print("🚀 Starting MCP backend server...")
    try:
        # Change to server directory
        os.chdir("server")
        
        # Start the server
        subprocess.run([sys.executable, "proxy.py"])
    except KeyboardInterrupt:
        print("\n⏹️  Server stopped by user")
    except Exception as e:
        print(f"❌ Failed to start server: {e}")

def main():
    """Main startup function"""
    print("🔧 MCP Chat Backend Startup")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Install dependencies
    if not install_requirements():
        print("❌ Failed to install dependencies. Please check your Python environment.")
        sys.exit(1)
    
    # Start server
    start_server()

if __name__ == "__main__":
    main()
