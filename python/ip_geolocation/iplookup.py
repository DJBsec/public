
#!/usr/bin/env python

import subprocess
import json
from rich.console import Console
from rich.table import Table

console = Console()
url = "https://json.geoiplookup.io/"
ip_address = input("IP Address = ")

# Construct the full URL
full_url = f"{url}{ip_address}"

# Run the curl command and capture the output
try:
    result = subprocess.run(['curl', full_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode == 0:
        # Parse the JSON response
        data = json.loads(result.stdout)
        
        # Create a Rich table for a user-friendly output
        table = Table(title="GeoIP Lookup Results", title_style="bold cyan")
        table.add_column("Key", style="bold green", no_wrap=True)
        table.add_column("Value", style="white")
        
        for key, value in data.items():
            table.add_row(key, str(value))
        
        # Print the table
        console.print(table)
    else:
        console.print(f"[red]Error:[/red] {result.stderr}")
except Exception as e:
    console.print(f"[bold red]An error occurred:[/bold red] {e}")
