def get_enterprise_metric(metric_name: str) -> str:
    """
    Retrieves enterprise financial or operational metrics from backend data systems.
    """
    metrics_db = {
        "global_revenue_pipeline": "Status: Active. Last run completed at 02:00 UTC with 99.8% data integrity across BigQuery tables.",
        "concession_score": "Current heuristic score: 0.84 (High retention likelihood based on 90-day activity logs).",
        "pnl_bridge": "Automated P&L bridge reports a net variance of +$1.2M quarter-over-quarter."
    }
    key = metric_name.lower().strip()
    return metrics_db.get(key, f"Metric '{metric_name}' not found in enterprise records.")

VERTEX_TOOLS = [
    {
        "name": "get_enterprise_metric",
        "description": "Retrieve enterprise financial, P&L, or operational metrics from backend systems.",
        "input_schema": {
            "type": "object",
            "properties": {
                "metric_name": {
                    "type": "string",
                    "description": "The enterprise metric name (e.g., 'global_revenue_pipeline', 'concession_score', 'pnl_bridge')"
                }
            },
            "required": ["metric_name"]
        }
    }
]
