from pathlib import Path
import json
import requests

from agents.tools.base_tool import BaseTool


class PipelineTool(BaseTool):

    name = "pipeline"

    description = "Pipeline Monitoring Tool"

    def execute(self):

        status = {}

        status["dbt"] = self.dbt_status()

        airflow = self.airflow_status()

        status["airflow"] = airflow

        return status

    def dbt_status(self):

        run_results = Path(
            "dbt_project/target/run_results.json"
        )

        if not run_results.exists():

            return {
                "status": "Not Found"
            }

        with open(run_results) as file:

            results = json.load(file)

        success = 0

        failed = 0

        for result in results["results"]:

            if result["status"] == "success":

                success += 1

            else:

                failed += 1

        return {

            "status": "Healthy" if failed == 0 else "Failed",

            "successful_models": success,

            "failed_models": failed,
        }



    def airflow_status(self):

        try:

            response = requests.get(
                "http://localhost:8080/api/v1/health",
                auth=("airflow", "airflow"),
                timeout=5,
            )

            if response.status_code == 200:

                return response.json()

            return {
                "status": "Unavailable",
                "status_code": response.status_code,
            }

        except Exception as exc:

            return {
                "status": "Offline",
                "error": str(exc),
            }