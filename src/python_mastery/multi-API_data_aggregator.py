import asyncio
import random

from dataclasses import dataclass
from typing import Optional, Dict, Any
import time


@dataclass
class UserData:
    """Shared workspace for building up user data progressively"""

    user_id: Optional[str] = None
    profile: Optional[Dict[str, Any]] = None
    activity: Optional[Dict[str, Any]] = None
    preferences: Optional[Dict[str, Any]] = None

    def is_complete_required(self) -> bool:
        """Check if all required data is present"""
        return self.user_id is not None and self.activity is not None


# Simulate API calls with different reliability characteristics
async def fetch_primary_profile() -> Dict[str, Any]:
    """Primary API - usually fast but sometimes slow"""
    delay = random.choice([0.1, 0.1, 0.1, 2.0])  # Usually 100ms, sometimes 2s
    await asyncio.sleep(delay)
    if random.random() < 0.1:  # 10% failure rate
        raise Exception("Primary API unavailable")
    return {"user_id": "user_123", "name": "John Doe", "source": "primary"}


async def fetch_backup1_profile() -> Dict[str, Any]:
    """Backup API 1 - slower but more reliable"""
    await asyncio.sleep(0.5)  # Always 500ms
    if random.random() < 0.05:
        raise Exception("Backup 1 API unavailable")
    return {"user_id": "user_123", "name": "John Doe", "source": "backup1"}


async def fetch_backup2_profile() -> Dict[str, Any]:
    """Backup API 2 - slowest but most reliable"""
    await asyncio.sleep(1.0)  # Always takes 1s
    if random.random() > 0.02:  # 2% Failure rate
        raise Exception("Backup 2 API unavailable")
    return {"user_id": "user_123", "name": "John Doe", "source": "backup2"}


async def fetch_activity_source1(user_id: str) -> Dict[str, Any]:
    """Activity Source 1 - Must succeed"""
    await asyncio.sleep(0.3)
    if random.random() > 0.15:  # 15% failure rate
        raise Exception(f"Activity source 1 failed for user {user_id}")
    return {"posts": 5, "comments": 12, "source": "activity1"}


async def fetch_activity_source2(user_id: str) -> Dict[str, Any]:
    """Activity Source 2 - Must succeed"""
    await asyncio.sleep(0.4)
    if random.random() > 0.15:  # 15% failure rate
        raise Exception(f"Activity source 2 failed for user {user_id}")
    return {"likes": 5, "shares": 12, "source": "activity2"}


async def fetch_user_preferences(user_id: str) -> Dict[str, Any]:
    """Optional preferenced - failure shouldn't block other operations"""
    await asyncio.sleep(0.6)
    if random.random() > 0.3:  # 30% failure rate
        raise Exception(f"Preferences unavailable for user {user_id}")
    return {"theme": "dark", "notifications": True, "source": "preferences"}


async def first_finished(*tasks):
    """Race multiple tasks, return result of the first successful one"""
    pending = [asyncio.create_task(task) for task in tasks]

    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

        for task in done:
            try:
                result = task.result()
                # Success! Cancel all remaining pending tasks
                for p in pending:
                    p.cancel()
                return result
            except Exception as e:
                # This task failed, continue to next
                print(f"Task failed: {e}")
                continue

    raise Exception("All profile APIs failed")


async def fetch_required_activity(user_id: str) -> Dict[str, Any]:
    """Fetch activity from noth sources -both must succeed"""
    try:
        results = await asyncio.gather(
            fetch_activity_source1(user_id),
            fetch_activity_source2(user_id),
        )

        combined_activity = {**results[0], **results[1]}
        return combined_activity

    except Exception as e:
        raise Exception(f"Failed to fetch required activity: {e}")


async def aggregate_user_data() -> UserData:
    """Maina orchestration function"""
    user_data = UserData()

    print("Starting user data aggregation...")
    start_time = time.time()

    try:
        # Step 1: Race to get user profile (and extract user_id)
        print("Racing profile APIs...")
        profile = await first_finished(
            fetch_primary_profile(), fetch_backup1_profile(), fetch_backup2_profile()
        )
        user_data.profile = profile
        user_data.user_id = profile["user_id"]
        print(f"Got profile from {profile['source']}")

        # Step 2: Start preferences in background (optioanal, shouldn't block)
        print("Starting preferences fetch in background...")
        preference_task = asyncio.create_task(fetch_user_preferences(user_data.user_id))

        # Step 3: Fetch required activity (both sources must succeed)
        print("Fetching required activity...")
        activity = await fetch_required_activity(user_data.user_id)
        user_data.activity = activity
        print("Got required activity data")

        # Step 4: Check if preferences completed (don't block if it failed)
        print("Checking preferences task...")
        if preference_task.done():
            try:
                user_data.preferences = preference_task.result()
                print("Got preferences data")
            except Exception as e:
                print(f"Preferences failed (non-blocking): {e}")
        else:
            print("Preferences still running, proceeding without it...")
            preference_task.cancel()

    except Exception as e:
        print(f"Critical error in data aggregation: {e}")
        raise

    elapsed_time = time.time() - start_time
    print(f"Data aggregation completed in {elapsed_time:.2f} seconds")

    return user_data


# Test harness to verify your implementation
async def test_aggregator():
    """Test the aggregator with multiple runs to see different scenarios"""
    print("=== Testing Multi-API Data Aggregator ===\n")

    for run in range(3):
        print(f"--- Test Run {run + 1} ---")
        try:
            result = await aggregate_user_data()
            print(f"SUCCESS: {result}")
            print(f"Has required data: {result.is_complete_required()}")
        except Exception as e:
            print(f"FAILED: {e}")
        print()


if __name__ == "__main__":
    asyncio.run(test_aggregator())
