# user_data_processor.py - WITH comprehensive type hints
import json
import requests
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Any, Optional, Union, TypedDict, Literal, Sequence


# Type definitions for better self-documentation
class RawUserData(TypedDict, total=False):
    """Raw user data from API - not all fields guaranteed"""

    id: int
    name: str
    email: str
    age: int
    status: str
    tags: List[str]
    metadata: Dict[str, Any]


class ProcessedUser(TypedDict):
    """Processed user with all required fields filled"""

    id: int
    name: str
    email: Optional[str]
    age: Optional[int]
    status: str
    tags: List[str]
    metadata: Dict[str, Any]


class ProcessingStats(TypedDict):
    """Statistics from processing operation"""

    total_processed: int
    by_status: Dict[str, int]


class ProcessingResult(TypedDict):
    """Complete result of user batch processing"""

    users: List[ProcessedUser]
    stats: ProcessingStats
    errors: List[str]
    metadata: Dict[str, Any]


class FilterCriteria(TypedDict, total=False):
    """Filter criteria for user processing - all optional"""

    min_age: int
    status: str
    # TODO: Add more filter types as needed (tags, email_domain, etc.)


# Type aliases for clarity
UserIdInput = Union[int, str]  # APIs often accept both
ReportFormat = Literal["json", "summary"]


def fetch_user_data(
    user_ids: Sequence[UserIdInput], include_metadata: bool = True, timeout: int = 30
) -> List[Optional[RawUserData]]:
    """
    Fetch user data from API with optional metadata

    Args:
        user_ids: Sequence of user IDs (int or str)
        include_metadata: Whether to include user metadata
        timeout: Request timeout in seconds

    Returns:
        List containing user data or None for failed requests

    Note:
        Using Sequence instead of List allows callers to pass
        tuples, lists, or other sequences
    """
    results: List[Optional[RawUserData]] = []

    for user_id in user_ids:
        try:
            url = f"https://api.example.com/users/{user_id}"
            params = {"include_meta": include_metadata}

            # Handle requests library typing issue
            response: requests.Response = requests.get(
                url, params=params, timeout=timeout
            )

            if response.status_code == 200:
                user_data: Dict[str, Any] = response.json()
                # We can't guarantee the API returns properly typed data
                # so we cast to our expected type but acknowledge uncertainty
                results.append(user_data)  # type: ignore[arg-type]
            else:
                results.append(None)
        except Exception as e:
            print(f"Error fetching user {user_id}: {e}")
            results.append(None)

    return results


def process_user_batch(
    raw_data: List[Optional[RawUserData]], filters: Optional[FilterCriteria] = None
) -> ProcessingResult:
    """
    Process raw user data with optional filtering

    Args:
        raw_data: List of user data from fetch_user_data
        filters: Optional filtering criteria

    Returns:
        ProcessingResult with users, stats, errors, and metadata
    """
    if filters is None:
        filters = {}

    # Initialize with proper typing
    processed: ProcessingResult = {
        "users": [],
        "stats": {"total_processed": 0, "by_status": defaultdict(int)},
        "errors": [],
        "metadata": {"processed_at": datetime.now(), "total_count": len(raw_data)},
    }

    for item in raw_data:
        if item is None:
            processed["errors"].append("Invalid user data")
            continue

        # Apply filters with proper type checking
        if "min_age" in filters:
            user_age = item.get("age", 0)
            if user_age < filters["min_age"]:
                continue

        if "status" in filters:
            user_status = item.get("status")
            if user_status != filters["status"]:
                continue

        # Process valid user with explicit typing
        user_info: ProcessedUser = {
            "id": item.get("id", 0),  # Provide defaults for required fields
            "name": item.get("name", "Unknown"),
            "email": item.get("email"),  # Can be None
            "age": item.get("age"),  # Can be None
            "status": item.get("status", "inactive"),
            "tags": item.get("tags", []),
            "metadata": item.get("metadata", {}),
        }

        processed["users"].append(user_info)
        processed["stats"]["by_status"][user_info["status"]] += 1
        processed["stats"]["total_processed"] += 1

    return processed


def generate_report(
    processed_data: ProcessingResult, format_type: ReportFormat = "json"
) -> str:
    """
    Generate report from processed data

    Args:
        processed_data: Result from process_user_batch
        format_type: Output format ('json' or 'summary')

    Returns:
        Formatted report string

    Raises:
        ValueError: If format_type is not supported
    """
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
        # This will never execute due to Literal typing, but good practice
        raise ValueError(f"Unsupported format: {format_type}")


def main() -> None:
    """Main execution function with explicit return type"""
    user_ids: List[UserIdInput] = [1, 2, 3, "invalid", 5]
    filters: FilterCriteria = {"min_age": 18, "status": "active"}

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
