# user_data_processor.py - BEFORE type hints
import json
import requests
from datetime import datetime
from collections import defaultdict


def fetch_user_data(user_ids, include_metadata=True, timeout=30):
    """Fetch user data from API with optional metadata"""
    results = []
    for user_id in user_ids:
        try:
            url = f"https://api.example.com/users/{user_id}"
            params = {"include_meta": include_metadata}
            response = requests.get(url, params=params, timeout=timeout)

            if response.status_code == 200:
                user_data = response.json()
                results.append(user_data)
            else:
                results.append(None)
        except Exception as e:
            print(f"Error fetching user {user_id}: {e}")
            results.append(None)

    return results


def process_user_batch(raw_data, filters=None):
    """Process raw user data with optional filtering"""
    if filters is None:
        filters = {}

    processed = {
        "users": [],
        "stats": defaultdict(int),
        "errors": [],
        "metadata": {"processed_at": datetime.now(), "total_count": len(raw_data)},
    }

    for item in raw_data:
        if item is None:
            processed["errors"].append("Invalid user data")
            continue

        # Apply filters
        if "min_age" in filters and item.get("age", 0) < filters["min_age"]:
            continue

        if "status" in filters and item.get("status") != filters["status"]:
            continue

        # Process valid user
        user_info = {
            "id": item["id"],
            "name": item.get("name", "Unknown"),
            "email": item.get("email"),
            "age": item.get("age"),
            "status": item.get("status", "inactive"),
            "tags": item.get("tags", []),
            "metadata": item.get("metadata", {}),
        }

        processed["users"].append(user_info)
        processed["stats"]["by_status"][user_info["status"]] += 1
        processed["stats"]["total_processed"] += 1

    return processed


def generate_report(processed_data, format_type="json"):
    """Generate report from processed data"""
    if format_type == "json":
        return json.dumps(processed_data, default=str, indent=2)
    elif format_type == "summary":
        stats = processed_data["stats"]
        return f"""
User Processing Report
======================
Total Processed: {stats['total_processed']}
Errors: {len(processed_data['errors'])}
Status Breakdown: {dict(stats['by_status'])}
Generated: {processed_data['metadata']['processed_at']}
"""
    else:
        raise ValueError(f"Unsupported format: {format_type}")


def main():
    user_ids = [1, 2, 3, "invalid", 5]
    filters = {"min_age": 18, "status": "active"}

    # Fetch data
    raw_data = fetch_user_data(user_ids, include_metadata=True)

    # Process data
    processed = process_user_batch(raw_data, filters)

    # Generate reports
    json_report = generate_report(processed, "json")
    summary_report = generate_report(processed, "summary")

    print("JSON Report:", json_report)
    print("Summary Report:", summary_report)


if __name__ == "__main__":
    main()
