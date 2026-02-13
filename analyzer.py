"""Creator Spark Registry
Micro-CRM for tracking which creators to cheer on."""
from rich import print
from statistics import mean

data = [
  {
    "name": "@fjordsketch",
    "heat": 0.87
  },
  {
    "name": "@auroraaudio",
    "heat": 0.92
  },
  {
    "name": "@northernknots",
    "heat": 0.74
  }
]

def summarize():
    avg = mean(entry['heat'] for entry in data)
    print(f"[bold cyan]Avg heat[/bold cyan]: {avg:.2f}")
    print("
[bold]Highlights[/bold]")
    for entry in sorted(data, key=lambda e: e['heat'], reverse=True)[:3]:
        print(f" • {entry['name']} -> {entry['heat']}")

if __name__ == '__main__':
    summarize()
