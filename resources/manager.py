import psutil
import subprocess


class ResourceManager:

    def get_cpu(self):
        return psutil.cpu_percent(interval=0.5)

    def get_ram(self):
        memory = psutil.virtual_memory()

        return {
            "percent": memory.percent,
            "available_gb": round(memory.available / (1024 ** 3), 2)
        }

    def get_gpu(self):
        try:
            result = subprocess.run(
                [
                    "nvidia-smi",
                    "--query-gpu=temperature.gpu,utilization.gpu,memory.used,memory.total",
                    "--format=csv,noheader,nounits"
                ],
                capture_output=True,
                text=True,
                timeout=5
            )

            values = result.stdout.strip().split(",")

            return {
                "temperature": int(values[0].strip()),
                "utilization": int(values[1].strip()),
                "memory_used_mb": int(values[2].strip()),
                "memory_total_mb": int(values[3].strip())
            }

        except Exception:
            return None

    def get_status(self):

        cpu = self.get_cpu()
        ram = self.get_ram()
        gpu = self.get_gpu()

        status = "normal"

        if gpu:

            if gpu["temperature"] >= 85:
                status = "critical"

            elif gpu["temperature"] >= 78:
                status = "high"

        if cpu >= 95 or ram["percent"] >= 95:
            status = "high"

        return {
            "cpu": cpu,
            "ram": ram,
            "gpu": gpu,
            "status": status
        }

    def recommended_agents(self):

        status = self.get_status()

        if status["status"] == "critical":
            return 0

        if status["status"] == "high":
            return 1

        return 3


resource_manager = ResourceManager()
