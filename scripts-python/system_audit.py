import os
import json
import platform
import datetime
import psutil


def get_system_info():
    return {
        "hostname": platform.node(),
        "os": platform.system(),
        "version": platform.release(),
        "architecture": platform.machine(),
        "timestamp": datetime.datetime.now().isoformat()
    }


def get_cpu_usage():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1)
    }


def get_memory_usage():
    mem = psutil.virtual_memory()
    return {
        "total_mb": round(mem.total / 1024 / 1024),
        "used_mb": round(mem.used / 1024 / 1024),
        "free_mb": round(mem.available / 1024 / 1024)
    }


def get_disk_usage():
    disk = psutil.disk_usage('/')
    return {
        "total_gb": round(disk.total / 1024 / 1024 / 1024),
        "used_gb": round(disk.used / 1024 / 1024 / 1024),
        "free_gb": round(disk.free / 1024 / 1024 / 1024)
    }


def run_audit():
    print("=== System Audit ===\n")

    report = {
        "system": get_system_info(),
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage()
    }

    # Afficher résumé
    print(f"Host     : {report['system']['hostname']}")
    print(f"OS       : {report['system']['os']} {report['system']['version']}")
    print(f"CPU      : {report['cpu']['cpu_percent']}%")
    print(f"Memory   : {report['memory']['used_mb']}MB / {report['memory']['total_mb']}MB")
    print(f"Disk     : {report['disk']['used_gb']}GB / {report['disk']['total_gb']}GB")

    # Créer dossier reports
    os.makedirs("reports", exist_ok=True)

    # Exporter JSON
    filename = f"reports/audit_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\nReport saved: {filename}")


if __name__ == "__main__":
    run_audit()
